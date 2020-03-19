from bs4 import BeautifulSoup
import urllib.request

class Course:
    def __init__(self, crn):
        self._crn = crn
        self.soup = self.get_soup()

    @property
    def crn(self):
        return str(self._crn)

    @property
    def title(self):
        title = self.soup.findAll("td", {"class": "crn_header"})[0].get_text() 
        return title.rstrip()

    @property
    def instructor(self):
        return 'Esmaail Nikjeh'

    @property
    def meeting_time(self):
        return 'Mon at 3:00pm-5:50pm'
    
    @property
    def location(self):
        return 'Moorpark Life Sci/Math/Comp 138'

    @property
    def status(self):
        status = self.soup.findAll('table')[2].findAll('tr')[3].find_all('td')[0].get_text()
        return status

    @property
    def waitlist_availability(self):
        return '5 out of 5 spots open'

    def get_html(self):
        crn = self.crn
        url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_listthislist'
        url_values = 'TERM=202007&TERM_DESC=Fall+2020&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_subj=%25&sel_crse=&sel_crn=' + crn + '&sel_title=&sel_ptrm=%25&sel_camp=%25&sel_instr=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&sel_new1=&aa=N&bb=N&dd=N&ee=N&ff=N&ztc=N'
        full_url = url + '?' + url_values
        html_doc = urllib.request.urlopen(full_url).read()
        return html_doc	

    def get_soup(self):
        plain_html = self.get_html()
        soup = BeautifulSoup(plain_html, 'html.parser')
        return soup