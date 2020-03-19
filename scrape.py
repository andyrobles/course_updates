from bs4 import BeautifulSoup
import urllib.request


def get_html(crn):
	url = 'https://ssb.vcccd.edu/prod/pw_pub_sched.p_listthislist'
	url_values = 'TERM=202007&TERM_DESC=Fall+2020&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_camp=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_subj=%25&sel_crse=&sel_crn=' + crn + '&sel_title=&sel_ptrm=%25&sel_camp=%25&sel_instr=%25&begin_hh=5&begin_mi=0&begin_ap=a&end_hh=11&end_mi=0&end_ap=p&sel_new1=&aa=N&bb=N&dd=N&ee=N&ff=N&ztc=N'
	full_url = url + '?' + url_values
	html_doc = urllib.request.urlopen(full_url).read()
	return html_doc	

def get_soup(crn):
	plain_html = get_html(crn)
	soup = BeautifulSoup(plain_html, 'html.parser')
	return soup

class StatusWatcher:
	def __init__(self, crn):
		soup = get_soup(crn)
		self.crn = crn
		self.title = get_title(soup)
		
	def watch(self):
		while True:
			soup = get_soup(self.crn)
			message = 'Title: ' + self.title + '\nProfessor: ' + self.professor + '\nMeeting Time: ' + self.days + ' ' + self.time + '\nLocation: ' + self.location + '\nStatus: ' + get_status(soup)
			print(message)
			print('')
			time.sleep(1)

	def thread(self):
		Thread(target = self.watch).start()

def remove_newlines(string):
	return string.replace('\n', '')

def get_status(soup): 
	status = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[0].get_text()
	return status

def get_title(soup):
	title = soup.findAll("td", {"class": "crn_header"})[0].get_text()
	return title

def get_professor(soup):
	professor = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[16].get_text()
	return professor

def get_time(soup):
	time = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[11].get_text()
	return time

def get_location(soup):
	location = soup.find_all('table')[2].find_all('tr')[3].find_all('td')[12].get_text()
	return location

def get_indexed_day(index, soup):
	return soup.find_all('table')[2].find_all('tr')[3].find_all('td')[4 + index].get_text()

def get_days(soup):
	days = ''
	for i in range(7):
		days = days + get_indexed_day(i, soup)
	days = days.replace(' ', '').replace('M', 'Mon').replace('T', ' Tues').replace('W', ' Wed').replace('R', ' Thurs').replace('F', ' Fri').replace('S', ' Sat')
	return days

def get_num_results(soup):
	return int(soup.center.get_text()[10])

def quick_watch():
	sw = StatusWatcher(DH_R040_CRN)
	sw.watch()


# soup = get_soup('73039')
# print(soup.prettify())

watcher = StatusWatcher('73039')
print(watcher.title)