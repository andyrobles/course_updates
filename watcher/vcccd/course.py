from bs4 import BeautifulSoup
import urllib.request

class CourseSnapshot:
    def __init__(self, crn):
        self._crn = crn
        self.course_search_results_soup = self.get_course_search_results_soup()
        self.course_details_soup = self.get_course_details_soup()

    @property
    def crn(self):
        return str(self._crn)

    @property
    def title(self):
        title = self.course_search_results_soup.findAll("td", {"class": "crn_header"})[0].get_text() 
        return title.rstrip()

    @property
    def instructor(self):
    	professor = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[16].get_text()
    	return professor

    @property
    def meeting_time(self):
        return '{} {}'.format(self._weekdays, self._time_span)

    def _weekday(self, index):
        weekday = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[4 + index].get_text()
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
        time = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[11].get_text()
        return time

    @property
    def location(self):
        location = self.course_search_results_soup.find_all('table')[2].find_all('tr')[3].find_all('td')[12].get_text()
        return location

    @property
    def status(self):
        status = self.course_search_results_soup.findAll('table')[2].findAll('tr')[3].find_all('td')[0].get_text()
        return status

    @property
    def waitlist_availability(self):
        return '{} out of {} spots open'.format(self._spots_left, self._total_spots)
        return waitlist_availability 

    @property
    def _spots_left(self):
        spots_left = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[3].get_text()
        return spots_left

    @property
    def _total_spots(self):
        total_spots = self.course_details_soup.find_all('table')[2].find_all('tr')[2].find_all('td')[5].get_text()
        return total_spots

    def get_course_search_results_html(self):
        crn = self.crn
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
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_course_popup?vsub=CS&vcrse=M10P&vterm=202007&vcrn={}'.format(self.crn)
        html_doc = urllib.request.urlopen(url).read()
        return html_doc

    def get_course_details_soup(self):
        plain_html = self.get_course_details_html()
        return BeautifulSoup(plain_html, 'html.parser')
    