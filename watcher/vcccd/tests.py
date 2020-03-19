import unittest
from course import Course 

class TestCRN71596(unittest.TestCase):
    def setUp(self):
        self.course = Course(71596)
        self.expected_values = {
            'crn': '71596',
            'title': 'CS M10P - Python Programming',
            'instructor': 'Nikjeh, Esmaail',
            'meeting_time': 'M 03:00pm - 05:50pm',
            'location': 'Moorpark Life Sci/Math/Comp 138', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        }

    def test_crn(self):
        self.assertEqual(self.course.crn, self.expected_values['crn'])

    def test_title(self):
        self.assertEqual(self.course.title, self.expected_values['title'])

    def test_instructor(self):
        self.assertEqual(self.course.instructor, self.expected_values['instructor'])

    def test_meeting_time(self):
        self.assertEqual(self.course.meeting_time, self.expected_values['meeting_time'])

    def test_location(self):
        self.assertEqual(self.course.location, self.expected_values['location'])

    def test_status(self):
        self.assertEqual(self.course.status, self.expected_values['status'])

    def test_waitlist_availability(self):
        self.assertEqual(self.course.waitlist_availability, self.expected_values['waitlist_availability'])


class TestCRN72525(unittest.TestCase):
    def setUp(self):
        self.course = Course(72525)
        self.expected_values = {
            'crn': '72525',
            'title': 'CS M15W - ClientSide WebD HTML/Javascrip',
            'instructor': 'Alnaji, Loay',
            'meeting_time': 'T, R 12:00pm - 02:15pm',
            'location': 'Health Science Center 103', 
            'status': 'OPEN',
            'waitlist_availability': '5 out of 5 spots open' 
        }

    def test_crn(self):
        self.assertEqual(self.course.crn, self.expected_values['crn'])

    def test_title(self):
        self.assertEqual(self.course.title, self.expected_values['title'])

    def test_instructor(self):
        self.assertEqual(self.course.instructor, self.expected_values['instructor'])

    def test_meeting_time(self):
        self.assertEqual(self.course.meeting_time, self.expected_values['meeting_time'])

    def test_location(self):
        self.assertEqual(self.course.location, self.expected_values['location'])

    def test_status(self):
        self.assertEqual(self.course.status, self.expected_values['status'])

    def test_waitlist_availability(self):
        self.assertEqual(self.course.waitlist_availability, self.expected_values['waitlist_availability'])

if __name__ == '__main__':
    unittest.main()