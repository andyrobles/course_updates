from bs4 import BeautifulSoup
import urllib.request

class CourseSearcher:
    """Purpose is to find course index which allows to later retrieve the a course in O(1) time."""

    def __init__(self, course_search_results_page=None):
        """Scrapes course data from VCCCD system and stores it in the class."""
        self.course_search_results_page = CourseScraper().scraped_data if not course_search_results_page else course_search_results_page

    def find_course(self, crn):
        """
        Searches scraped data to find the course by given CRN.

        Parameters:
            crn (int): The crn, or Course Reference Number, is the 5-digit number assigned to each course in the VCCCD system.

        Returns
            dict: course attributes as keys and parsed info as values.
        """
        self._crn_table_data = self.course_search_results_page.find('a', text='{} '.format(str(crn)))
        self._status_table_data = self._crn_table_data.find_parent('td').find_previous_sibling('td')
        course_attributes = self._basic_course_attributes

        if self._is_distance_education_course:
            course_attributes.update(self._distance_education_course_attributes)
        else:
            course_attributes.update(self._standard_meeting_course_attributes)

        return course_attributes

    @property
    def _is_distance_education_course(self):
        """Returns True if this course is a distance education course and false otherwise."""
        return True if 'Distance' in self._parse_course_row(4) else False

    @property
    def _standard_meeting_course_attributes(self):
        """
        Handles attribute parsing for a course that meets on campus.
        
        Returns:
            dict: course attributes as keys and parsed info as values.
        """
        return {
            'instructor': self._parse_course_row(16),
            'meeting_time': self._meeting_time,
            'location': self._parse_course_row(12),
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
            'location': self._parse_course_row(5),
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
            'crn': self._crn_table_data.get_text().strip(), 
            'title': self._status_table_data.find_parent('tr').find_previous('td', class_='crn_header').get_text().strip(),
            'status': self._parse_course_row(0),
        }

    @property
    def _meeting_time(self):
        table_data = self._status_table_data.find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td')
        substring = ''
        num_days = 0
        for i in range(8):
            text = table_data.get_text().strip()
            num_days += 1
            if num_days == 8:
                substring = '{} {}'.format(substring, text)
            elif text != '':
                substring = '{}, {}'.format(substring, text)
            else:
                substring = '{}{}'.format(substring, text)
            table_data = table_data.find_next_sibling('td')
        substring = substring.strip(',')
        return substring.strip()
    
    def _parse_course_row(self, n):
        """Traverses adjacent table data siblings n times and returns text"""
        table_data = self._status_table_data
        for i in range(n):
            table_data = table_data.find_next_sibling('td')

        return table_data.get_text().strip()

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


class CourseSnapshot:
    def __init__(self, crn):
        """
        Parameters:
            crn (int): CRN of course to scrape and bind to this class.
        """
        self._course_attributes = CourseSearcher().find_course(crn)

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
