from bs4 import BeautifulSoup
import urllib.request

class CourseSearcher:
    """Purpose is to find course index which allows to later retrieve the a course in O(1) time."""

    def __init__(self, course_search_results_page=None):
        """Scrapes course data from VCCCD system and stores it in the class."""
        self.course_search_results_page = CourseScraper().scraped_data if not course_search_results_page else course_search_results_page
        self._parser = CourseParser(course_search_results_page)

    def find_index(self, crn):
        """
        Searches scraped data to find the course and stores the index.

        Parameters:
            crn (int): The crn, or Course Reference Number, is the 5-digit number assigned to each course in the VCCCD system.
        """
        for i in range(20):
            course_attributes = self._parser.get_course_attributes(i)
            if str(crn) == course_attributes['crn']:
                return i

        return 1000

class CourseScraper:
    """Scrapes course data from VCCCD System and stores it in the class"""

    def __init__(self, crn=None):
        """
        Parameters:
            crn (int): The crn, or Course Reference Number, is the 5-digit number assigned to each course in the VCCCD system.
        """
        if crn == None:
            crn = ''
        self._crn = crn
        self.course_search_results_page = self.get_course_search_results_page()

    @property
    def scraped_data(self):
        return self.course_search_results_page

    def get_course_search_results_html(self):
        crn = str(self._crn) 
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_listthislist'
        url_values = 'TERM=202007&TERM_DESC=Fall+2020&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_subj=%25&sel_crse=&sel_crn=' + crn + '&sel_title=&sel_ptrm=%25&sel_camp=%25&sel_instr=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&sel_new1=&aa=N&bb=N&dd=N&ee=N&ff=N&ztc=N'
        full_url = url + '?' + url_values
        html_doc = urllib.request.urlopen(full_url).read()
        return html_doc	

    def get_course_search_results_page(self):
        plain_html = self.get_course_search_results_html()
        course_search_results_page = BeautifulSoup(plain_html, 'html.parser')
        return course_search_results_page

class CourseParser:
    """Parses course data and converts it to python variables"""

    def __init__(self, course_search_results_page):
        """
        Parameters:
            course_search_results_page (str): Raw scraped data of page that comes after course search submit.
            course_details_page (str): Raw scraped data of page that comes after clicking more info of course search result.
        """
        self.course_search_results_page = course_search_results_page
        self._clean_data()
        self._index = 0

    def _clean_data(self):
        """
        Removes table rows that contain subject headers.
        
        Returns:
            BeautifulSoup: Cleaned course results.
        """
        for table_row in self.course_search_results_page.find_all('td', class_='subject_header'):
            table_row.find_parent('tr').decompose()

    def get_course_attributes(self, index):
        """
        Parameters:
            index (int): A number specifying which course to return with respect to its order on the course results page.

        Returns:
            dict: course attributes as keys and parsed info as values.
        """
        self._index = index
        course_attributes = self._basic_course_attributes

        if self._is_distance_education_course():
            course_attributes.update(self._distance_education_course_attributes)
        else:
            course_attributes.update(self._standard_meeting_course_attributes)

        return course_attributes

    @property
    def _standard_meeting_course_attributes(self):
        """
        Handles attribute parsing for a course that meets on campus.
        
        Returns:
            dict: course attributes as keys and parsed info as values.
        """
        return {
            'instructor': self._parse_course_row(16),
            'meeting_time': '{} {}'.format(self._weekdays, self._time_span),
            'location': self._parse_course_row(12).strip(),
            'seating_availability': '{} out of {} spots open'.format(self._parse_course_row(15), self._parse_course_row(13))
        }

    @property
    def _distance_education_course_attributes(self):
        """
        Handles attribute parsing for a distance education class.
        
        Returns:
            dict: course attributes as keys and parsed info as values.
        """
        return {
            'instructor': self._parse_course_row(9),
            'meeting_time': 'Distance Education Class',
            'location': self._parse_course_row(5).strip(),
            'seating_availability': '{} out of {} spots open'.format(self._parse_course_row(8), self._parse_course_row(6))
        }

    @property
    def _basic_course_attributes(self):
        """
        Handles parsing for basic attributes with html arrangement common across all course types

        Returns:
            dict: course attributes as keys and parsed info as values
        """
        return {
            'crn': self._parse_course_row(1).strip(), 
            'title': self.course_search_results_page.findAll("td", {"class": "crn_header"})[0].get_text().rstrip(),
            'status': self._parse_course_row(0),
        }

    def _parse_course_row(self, column_index):
        return self._parse_course_search_results(2, 2 + self._index * 3, column_index)
    
    def _parse_scraped_data(self, scraped_data, table_index, tr_index, td_index):
        return scraped_data.find_all('table')[table_index].find_all('tr')[tr_index].find_all('td')[td_index].get_text()

    def _parse_course_search_results(self, table_index, tr_index, td_index):
        return self._parse_scraped_data(self.course_search_results_page, table_index, tr_index, td_index)

    def _weekday(self, index):
        weekday = self._parse_course_row(4 + index)
        return weekday

    @property
    def _weekdays(self):
        substring = ''
        num_weeks = 0
        for i in range(7):
            current_weekday = self._weekday(i)
            if current_weekday in ['M', 'T', 'W', 'R', 'F', 'S']:
                num_weeks += 1
                if num_weeks == 1:
                    substring = current_weekday
                else:
                    substring = '{}, {}'.format(substring, current_weekday)
        
        return substring

    @property
    def _time_span(self):
        time = self._parse_course_row(11)
        return time
    
    def _is_distance_education_course(self):
        # There are fewer cells in location meeting time column when an online course
        return len(self._weekday(0)) > 5 

class CourseSnapshot:
    def __init__(self, crn):
        self.course_search_results_page = CourseScraper(crn).scraped_data
        self._course_attributes = CourseParser(self.course_search_results_page).get_course_attributes(0)

    @property
    def crn(self):
        return self._course_attributes['crn']

    @property
    def title(self):
        return self._course_attributes['title']

    @property
    def instructor(self):
        return self._course_attributes['instructor']

    @property
    def meeting_time(self):
        return self._course_attributes['meeting_time']
    
    @property
    def location(self):
        return self._course_attributes['location']

    @property
    def status(self):
        return self._course_attributes['status']

    @property
    def seating_availability(self):
        return self._course_attributes['seating_availability']

    @property
    def waitlist_availability(self):
        return self._course_attributes['waitlist_availability']
