import unittest
from bs4 import BeautifulSoup
from course import CourseSnapshot, CourseSearcher

EXPECTED_COURSE_ATTRIBUTES = [
    {
        'crn': '71596',
        'title': 'CS M10P - Python Programming',
        'instructor': 'Nikjeh, Esmaail',
        'meeting_time': 'M 03:00pm - 05:50pm',
        'location': 'Moorpark Life Sci/Math/Comp 138', 
        'status': 'OPEN',
        'seating_availability': '35 out of 35 spots open',
    },
    {
        'crn': '73039',
        'title': 'CS M01 - Intro Computer Science',
        'instructor': 'Alnaji, Loay',
        'meeting_time': 'Distance Education Class',
        'location': 'Moorpark Online/Internet',
        'status': 'OPEN',
        'seating_availability': '55 out of 55 spots open',
    }
]

class TestCourseSnapshot(unittest.TestCase):
    def setUp(self):
        self.course_list = [CourseSnapshot(int(course_details['crn'])) for course_details in EXPECTED_COURSE_ATTRIBUTES]
        self.actual_and_expected = zip(self.course_list, EXPECTED_COURSE_ATTRIBUTES)

    def test_courses(self):
        for current_pair in self.actual_and_expected:
            self.assertEqual(current_pair[0].crn, current_pair[1]['crn'])
            self.assertEqual(current_pair[0].title, current_pair[1]['title'])
            self.assertEqual(current_pair[0].instructor, current_pair[1]['instructor'])
            self.assertEqual(current_pair[0].meeting_time, current_pair[1]['meeting_time'])
            self.assertEqual(current_pair[0].location, current_pair[1]['location'])
            self.assertEqual(current_pair[0].status, current_pair[1]['status'])
            self.assertEqual(current_pair[0].seating_availability, current_pair[1]['seating_availability'])


class TestCourseSearcher(unittest.TestCase):
    def setUp(self):
        self.course_searcher = CourseSearcher(self._mock_course_search_results)

    @property
    def _mock_course_search_results(self):
        """Imports data from adjacent file as BeautifulSoup"""

        ADJACENT_FILENAME = 'mock_course_search_results_raw_html_SMALL.txt'

        adjacent_file = open(ADJACENT_FILENAME, "r")
        raw_html = adjacent_file.read()
        adjacent_file.close()

        return BeautifulSoup(raw_html, 'html.parser')

    def test_course_index_0(self):
        expected_course = {
            'crn': '71941',
            'title': 'AB R001 - Auto Body/Fender Repair I',
            'instructor': 'Ortega, Jose',
            'meeting_time': 'T, R 08:00am - 11:50am',
            'location': 'Oxnard Auto Technology 1', 
            'status': 'OPEN',
            'seating_availability': '25 out of 25 spots open',
        }

        self.assertEqual(expected_course, self.course_searcher.find_course(71941))

    def test_course_index_1(self):
        expected_course = {
            'crn': '72024',
            'title': 'AB R003 - Estimating Damage/Repair',
            'instructor': 'Ortega, Jose',
            'meeting_time': 'M, F 08:00am - 11:50am',
            'location': 'Oxnard Auto Technology 1', 
            'status': 'OPEN',
            'seating_availability': '22 out of 22 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(72024))

    def test_course_index_2(self):
        expected_course = {
            'crn': '71925',
            'title': 'AB R005A - Painting & Refinishing I',
            'instructor': 'Ortega, Jose',
            'meeting_time': 'W 08:00am - 11:50am',
            'location': 'Oxnard Auto Technology 1', 
            'status': 'OPEN',
            'seating_availability': '25 out of 25 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(71925))

    def test_course_index_3(self):
        expected_course = {
            'crn': '70547',
            'title': 'AB R007A - Automotive Graphics',
            'instructor': 'Staff',
            'meeting_time': 'R 06:00pm - 09:50pm',
            'location': 'Oxnard Auto Technology', 
            'status': 'OPEN',
            'seating_availability': '25 out of 25 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(70547))

    def test_course_index_4(self):
        expected_course = {
            'crn': '71299',
            'title': 'AC R010 - Intro to Air Con & Ref',
            'instructor': 'Ainsworth, Alan',
            'meeting_time': 'W 07:00pm - 09:50pm',
            'location': 'Oxnard Occupational Education 9', 
            'status': 'OPEN',
            'seating_availability': '25 out of 25 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(71299))

    def test_course_index_5(self):
        expected_course = {
            'crn': '71452',
            'title': 'AC R010L - Intro Air Con & Ref I Lab',
            'instructor': 'Stewart, James',
            'meeting_time': 'W 03:00pm - 06:50pm',
            'location': 'Oxnard Occupational Education 9', 
            'status': 'OPEN',
            'seating_availability': '27 out of 27 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(71452))

    def test_course_index_11(self):
        expected_course = {
            'crn': '70571',
            'title': 'ACCT M01 - Introduction to Accounting',
            'instructor': 'Macias, Shannon',
            'meeting_time': 'Distance Education Class',
            'location': 'Moorpark Online/Internet', 
            'status': 'OPEN',
            'seating_availability': '55 out of 55 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(70571))

    def test_course_index_12(self):
        expected_course = {
            'crn': '71289',
            'title': 'ACCT M01 - Introduction to Accounting',
            'instructor': "D'Amico, Sabine",
            'meeting_time': 'W 06:00pm - 09:50pm',
            'location': 'Moorpark Technology/Business 216', 
            'status': 'OPEN',
            'seating_availability': '40 out of 40 spots open',
        }
        self.assertEqual(expected_course, self.course_searcher.find_course(71289))

if __name__ == '__main__':
    unittest.main()