import unittest
from course import CourseSnapshot, CourseSearch

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


class TestCourseSearch(unittest.TestCase):
    def setUp(self):
        self.course_search = CourseSearch()

    def test_ab_r001_crn_71941_is_0th_index(self):
        self.assertEqual(0, self.course_search.find_index(71941))

    def test_ab_r003_crn_72024_is_1st_index(self):
        self.assertEqual(1, self.course_search.find_index(72024))

    def test_ac_r010_crn_71299_is_4th_index(self):
        self.assertEqual(4, self.course_search.find_index(71299))

    def test_ac_r010l_crn_71452_is_5th_index(self):
        self.assertEqual(4, self.course_search.find_index(71452))

    def test_acct_m01_crn_70571_is_11th_index(self):
        self.assertEqual(11, self.course_search.find_index(70571))

    def test_acct_m01_crn_71289_is_12th_index(self):
        self.assertEqual(12, self.course_search.find_index(71289))

if __name__ == '__main__':
    unittest.main()