import sys

sys.path.append('./src')

from lab01 import *

def test_sort_by_courses_registered_02():
    students = [
        Student(given_name='lvwmN', surname='dmQ', registered_courses=['CO086']), \
        Student(given_name='OcA', surname='sPOAWMHLqF', registered_courses=['CO000', 'CO172', 'CO313']), \
        Student(given_name='PfURfBo', surname='iVSn', registered_courses=['CO977', 'CO279', 'CO549', 'CO427']), \
        Student(given_name='uVzm', surname='SENjfNM', registered_courses=['CO141']), \
        Student(given_name='pHozY', surname='hugVGi', registered_courses=['CO671', 'CO280'])
    ]

    expected = [
        Student(given_name='PfURfBo', surname='iVSn', registered_courses=['CO977', 'CO279', 'CO549', 'CO427']), \
        Student(given_name='OcA', surname='sPOAWMHLqF', registered_courses=['CO000', 'CO172', 'CO313']), \
        Student(given_name='pHozY', surname='hugVGi', registered_courses=['CO671', 'CO280']), \
        Student(given_name='lvwmN', surname='dmQ', registered_courses=['CO086']), \
        Student(given_name='uVzm', surname='SENjfNM', registered_courses=['CO141'])
    ]

    actual = sort_by_courses_registered(students)
    assert len(actual) == len(expected)
    assert type(actual) == list

    for actual_student_obj, expected_student_obj in zip(actual, expected):
        assert actual_student_obj == expected_student_obj