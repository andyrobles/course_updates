import unittest
from course import CourseSnapshot 

EXPECTED_COURSE_ATTRIBUTES = [
    {
        'key': 71596,
        'crn': '71596',
        'title': 'CS M10P - Python Programming',
        'instructor': 'Nikjeh, Esmaail',
        'meeting_time': 'M 03:00pm - 05:50pm',
        'location': 'Moorpark Life Sci/Math/Comp 138', 
        'status': 'OPEN',
        'seating_availability': '35 out of 35 spots open',
        'waitlist_availability': '5 out of 5 spots open' 
    },
]

class TestCourseAttributes(unittest.TestCase):
    def setUp(self):
        self.course_list = [CourseSnapshot(course_details['key']) for course_details in EXPECTED_COURSE_ATTRIBUTES]
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
            self.assertEqual(current_pair[0].waitlist_availability, current_pair[1]['waitlist_availability'])

if __name__ == '__main__':
    unittest.main()