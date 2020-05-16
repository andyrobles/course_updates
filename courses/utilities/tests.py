import unittest
from bs4 import BeautifulSoup
from .course import CourseSnapshot

EXPECTED_COURSE_ATTRIBUTES = [
    {
        'crn': '71596',
        'title': 'CS M10P - Python Programming',
        'instructor': 'Nikjeh, Esmaail',
        'meeting_time': 'M 03:00pm - 05:50pm',
        'location': 'Moorpark Life Sci/Math/Comp 138', 
        'status': 'OPEN',
        'seating_availability': '10 out of 35 spots open',
    },
    {
        'crn': '73039',
        'title': 'CS M01 - Intro Computer Science',
        'instructor': 'Alnaji, Loay',
        'meeting_time': 'Distance Education Class',
        'location': 'Moorpark Online/Internet',
        'status': 'Waitlisted',
        'seating_availability': '0 out of 55 spots open',
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

if __name__ == '__main__':
    unittest.main()