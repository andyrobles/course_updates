from bs4 import BeautifulSoup
import urllib.request

class CourseSnapshot:
    def __init__(self, crn):
        self._crn = crn
        self.course_search_results_soup = self.get_course_search_results_soup()
        self.course_details_soup = self.get_course_details_soup()
        self._course_attributes = {
            'crn': self._get_crn,
            'title': self._get_title,
            'instructor': self._get_instructor,
            'meeting_time': self._get_meeting_time,
            'location': self._get_location,
            'status': self._get_status,
            'seating_availability': self._get_seating_availability,
            'waitlist_availability': self._get_waitlist_availability
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

    @property
    def _get_crn(self):
        return str(self._crn)

    @property
    def _get_title(self):
        title = self.course_search_results_soup.findAll("td", {"class": "crn_header"})[0].get_text() 
        return title.rstrip()

    @property
    def _get_instructor(self):
        if self._is_distance_education_class():
    	    return  self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[9].get_text()
        else:
            return self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[16].get_text()

    @property
    def _get_meeting_time(self):
        if self._is_distance_education_class():
            return 'Distance Education Class'
        return '{} {}'.format(self._weekdays, self._time_span)

    def _weekday(self, index):
        weekday = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[4 + index].get_text()
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
        time = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[11].get_text()
        return time

    @property
    def _get_location(self):
        if self._is_distance_education_class():
            location = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[5].get_text()
        else:
            location = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[12].get_text()
        return location.strip()

    @property
    def _get_status(self):
        status = self.course_search_results_soup.findAll('table')[2].findAll('tr')[3].find_all('td')[0].get_text()
        return status

    @property
    def _get_seating_availability(self):
        return '{} out of {} spots open'.format(self._seating_spots_left, self._total_seating_spots)

    @property
    def _seating_spots_left(self):
        spots_left = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[2].get_text()
        return spots_left

    @property
    def _total_seating_spots(self):
        total_spots = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[0].get_text()
        return total_spots

    @property
    def _get_waitlist_availability(self):
        return '{} out of {} spots open'.format(self.waitlist_spots_left, self._total_waitlist_spots)

    @property
    def waitlist_spots_left(self):
        spots_left = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[5].get_text()
        return spots_left

    @property
    def _total_waitlist_spots(self):
        total_spots = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[3].get_text()
        return total_spots

    def get_course_search_results_html(self):
        crn = self._get_crn
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
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_course_popup?vsub=CS&vcrse=M10P&vterm=202007&vcrn={}'.format(self._get_crn)
        html_doc = urllib.request.urlopen(url).read()
        return html_doc

    def get_course_details_soup(self):
        plain_html = self.get_course_details_html()
        return BeautifulSoup(plain_html, 'html.parser')
