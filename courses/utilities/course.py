from bs4 import BeautifulSoup
import urllib.request

class CourseSearch:
    """
    Purpose is to find course index which allows to later retrieve the a course in O(1) time.
    """
    def __init__(self):
        """
        Scrapes course data from VCCCD system and stores it in the class.
        """
        pass

    def find_index(self, crn):
        """
        Searches scraped data to find the course and stores the index.

        Parameters:
            crn : The crn, or Course Reference Number, is the 5-digit number assigned to each course in the VCCCD system.
        """
        pass

class CourseSnapshot:
    def __init__(self, crn):
        self._crn = crn
        self.course_search_results_soup = self.get_course_search_results_soup()
        self.course_details_soup = self.get_course_details_soup()
        self._course_attributes = self._parse_course_attributes() 

    def _parse_course_attributes(self):
        return {
            'crn': str(self._crn), 
            'title': self.course_search_results_soup.findAll("td", {"class": "crn_header"})[0].get_text().rstrip(),
            'instructor': self._parse_course_search_results(2, 3, 9) if self._is_distance_education_class() else self._parse_course_search_results(2, 3, 16),
            'meeting_time': 'Distance Education Class' if self._is_distance_education_class() else '{} {}'.format(self._weekdays, self._time_span),
            'location': self._parse_course_search_results(2, 3, 5).strip() if self._is_distance_education_class() else self._parse_course_search_results(2, 3, 12).strip(),
            'status': self._parse_course_search_results(2, 3, 0),
            'seating_availability': '{} out of {} spots open'.format(self._parse_course_details(2, 2, 2), self._parse_course_details(2, 2, 0)),
            'waitlist_availability': '{} out of {} spots open'.format(self._parse_course_details(2, 2, 5), self._parse_course_details(2, 2, 3)),
        }

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

    def _parse_scraped_data(self, scraped_data, table_index, tr_index, td_index):
        return scraped_data.find_all('table')[table_index].find_all('tr')[tr_index].find_all('td')[td_index].get_text()

    def _parse_course_search_results(self, table_index, tr_index, td_index):
        return self._parse_scraped_data(self.course_search_results_soup, table_index, tr_index, td_index)

    def _parse_course_details(self, table_index, tr_index, td_index):
        return self._parse_scraped_data(self.course_details_soup, table_index, tr_index, td_index)

    def _weekday(self, index):
        weekday = self._parse_course_search_results(2, 3, 4 + index)
        return weekday

    def _is_distance_education_class(self):
        # There are fewer cells in location meeting time column when an online course
        return len(self._weekday(0)) > 5 

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
        time = self._parse_course_search_results(2, 3, 11)
        return time

    def get_course_search_results_html(self):
        crn = str(self._crn) 
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_listthislist'
        url_values = 'TERM=202007&TERM_DESC=Fall+2020&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_subj=%25&sel_crse=&sel_crn=' + crn + '&sel_title=&sel_ptrm=%25&sel_camp=%25&sel_instr=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&sel_new1=&aa=N&bb=N&dd=N&ee=N&ff=N&ztc=N'
        full_url = url + '?' + url_values
        html_doc = urllib.request.urlopen(full_url).read()
        return html_doc	

    def get_course_search_results_soup(self):
        plain_html = self.get_course_search_results_html()
        course_search_results_soup = BeautifulSoup(plain_html, 'html.parser')
        return course_search_results_soup

    def get_course_details_html(self):
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_course_popup?vsub=CS&vcrse=M10P&vterm=202007&vcrn={}'.format(str(self._crn))
        html_doc = urllib.request.urlopen(url).read()
        return html_doc

    def get_course_details_soup(self):
        plain_html = self.get_course_details_html()
        return BeautifulSoup(plain_html, 'html.parser')
    