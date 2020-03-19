import unittest
from course import Course 

EXPECTED_COURSE_ATTRIBUTES = [
        {
            'key': 71596,
            'crn': '71596',
            'title': 'CS M10P - Python Programming',
            'instructor': 'Nikjeh, Esmaail',
            'meeting_time': 'M 03:00pm - 05:50pm',
            'location': 'Moorpark Life Sci/Math/Comp 138', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        },
        {   
            'key': 72525,
            'crn': '72525',
            'title': 'CS M15W - ClientSide WebD HTML/JavaScrip',
            'instructor': 'Alnaji, Loay',
            'meeting_time': 'T, R 12:00pm - 02:15pm',
            'location': 'Health Science Center 103', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        },
        {   
            'key': 72522,
            'crn': '72522',
            'title': 'CS M10DB - Database Mgmt Systems and App',
            'instructor': 'Nikjeh, Esmaail',
            'meeting_time': 'T, W 12:00pm - 01:50pm',
            'location': 'Moorpark Life Sci/Math/Comp 138', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        },
        {   
            'key': 72506,
            'crn': '72506',
            'title': 'CS M125 - Prog Concepts Methodology I',
            'instructor': 'Alnaji, Loay',
            'meeting_time': 'M 09:00am - 11:50am',
            'location': 'Moorpark Life Sci/Math/Comp 138', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        }
    ]

class TestCourseAttributes(unittest.TestCase):
    def setUp(self):
        self.course_list = [Course(course_details['key']) for course_details in EXPECTED_COURSE_ATTRIBUTES]
        self.actual_and_expected = zip(self.course_list, EXPECTED_COURSE_ATTRIBUTES)

    def test_courses(self):
        for current_pair in self.actual_and_expected:
            self.assertEqual(current_pair[0].crn, current_pair[1]['crn'])
            self.assertEqual(current_pair[0].title, current_pair[1]['title'])
            self.assertEqual(current_pair[0].instructor, current_pair[1]['instructor'])
            self.assertEqual(current_pair[0].meeting_time, current_pair[1]['meeting_time'])
            self.assertEqual(current_pair[0].location, current_pair[1]['location'])
            self.assertEqual(current_pair[0].status, current_pair[1]['status'])
            self.assertEqual(current_pair[0].waitlist_availability, current_pair[1]['waitlist_availability'])

if __name__ == '__main__':
    unittest.main()