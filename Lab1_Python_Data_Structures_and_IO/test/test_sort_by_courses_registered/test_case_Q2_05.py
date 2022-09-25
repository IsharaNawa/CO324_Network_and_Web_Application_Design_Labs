import sys

sys.path.append('./src')

from lab01 import *

def test_sort_by_courses_registered_05():
    students = [
        Student(given_name='UcEki', surname='uYKVmjzXrI', registered_courses=[]), \
        Student(given_name='XopTMoflRk', surname='GgVjbhV', registered_courses=['CO310']), \
        Student(given_name='jED', surname='nigDsctTbU', registered_courses=['CO878', 'CO770', 'CO738', 'CO095']), \
        Student(given_name='kVgvzk', surname='tatt', registered_courses=['CO932', 'CO045', 'CO563', 'CO719', 'CO278']), \
        Student(given_name='OAQJ', surname='JwUKHANw', registered_courses=['CO023', 'CO742', 'CO278', 'CO758', 'CO971'])
    ]

    expected = [
        Student(given_name='kVgvzk', surname='tatt', registered_courses=['CO932', 'CO045', 'CO563', 'CO719', 'CO278']), \
        Student(given_name='OAQJ', surname='JwUKHANw', registered_courses=['CO023', 'CO742', 'CO278', 'CO758', 'CO971']), \
        Student(given_name='jED', surname='nigDsctTbU', registered_courses=['CO878', 'CO770', 'CO738', 'CO095']), \
        Student(given_name='XopTMoflRk', surname='GgVjbhV', registered_courses=['CO310']), \
        Student(given_name='UcEki', surname='uYKVmjzXrI', registered_courses=[])
    ]

    actual = sort_by_courses_registered(students)
    assert len(actual) == len(expected)
    assert type(actual) == list

    for actual_student_obj, expected_student_obj in zip(actual, expected):
        assert actual_student_obj == expected_student_obj