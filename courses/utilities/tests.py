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
        self.course_search = CourseSearcher(self._mock_course_search_results)

    @property
    def _mock_course_search_results(self):
        """Imports data from adjacent file as BeautifulSoup"""

        ADJACENT_FILENAME = 'mock_course_search_results_raw_html_SMALL.txt'

        adjacent_file = open(ADJACENT_FILENAME, "r")
        raw_html = adjacent_file.read()
        adjacent_file.close()

        return BeautifulSoup(raw_html, 'html.parser')

    def test_0th_index(self):
        self.assertEqual(1, self.course_search.find_index(71941))

    def test_1st_index(self):
        self.assertEqual(1, self.course_search.find_index(72024))

    def test_4th_index(self):
        self.assertEqual(4, self.course_search.find_index(71299))

    def test_5th_index(self):
        self.assertEqual(5, self.course_search.find_index(71452))

    def test_11th_index(self):
        self.assertEqual(11, self.course_search.find_index(70571))

    def test_12th_index(self):
        self.assertEqual(12, self.course_search.find_index(71289))

if __name__ == '__main__':
    unittest.main()