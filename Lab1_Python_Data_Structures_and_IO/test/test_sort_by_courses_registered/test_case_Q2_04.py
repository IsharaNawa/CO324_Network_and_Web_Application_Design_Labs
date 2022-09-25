import sys

sys.path.append('./src')

from lab01 import *

def test_sort_by_courses_registered_04():
    students = [
        Student(given_name='XgIIAT', surname='mSlwtsbD', registered_courses=['CO019', 'CO171', 'CO007']), \
        Student(given_name='IiaMmP', surname='sJmQUJHoS', registered_courses=['CO422', 'CO960', 'CO728', 'CO293', 'CO939']), \
        Student(given_name='ALiWi', surname='yOcC', registered_courses=['CO599', 'CO611', 'CO836']), \
        Student(given_name='GyzQVTZg', surname='IKcO', registered_courses=['CO157']), \
        Student(given_name='NNjxJqPic', surname='JeRGhbgrUQ', registered_courses=[]), \
        Student(given_name='WEUbBFGFNR', surname='jETbApw', registered_courses=['CO846', 'CO355', 'CO961', 'CO841']), \
        Student(given_name='jmWhBE', surname='JBdekZYW', registered_courses=['CO140', 'CO796', 'CO394', 'CO366']), \
        Student(given_name='PbV', surname='rgX', registered_courses=['CO669', 'CO944', 'CO690', 'CO494']), \
        Student(given_name='TPLcHkHEb', surname='EHCqETshVr', registered_courses=['CO642', 'CO082'])
    ]

    expected = [
        Student(given_name='IiaMmP', surname='sJmQUJHoS', registered_courses=['CO422', 'CO960', 'CO728', 'CO293', 'CO939']), \
        Student(given_name='WEUbBFGFNR', surname='jETbApw', registered_courses=['CO846', 'CO355', 'CO961', 'CO841']), \
        Student(given_name='jmWhBE', surname='JBdekZYW', registered_courses=['CO140', 'CO796', 'CO394', 'CO366']), \
        Student(given_name='PbV', surname='rgX', registered_courses=['CO669', 'CO944', 'CO690', 'CO494']), \
        Student(given_name='XgIIAT', surname='mSlwtsbD', registered_courses=['CO019', 'CO171', 'CO007']), \
        Student(given_name='ALiWi', surname='yOcC', registered_courses=['CO599', 'CO611', 'CO836']), \
        Student(given_name='TPLcHkHEb', surname='EHCqETshVr', registered_courses=['CO642', 'CO082']), \
        Student(given_name='GyzQVTZg', surname='IKcO', registered_courses=['CO157']), \
        Student(given_name='NNjxJqPic', surname='JeRGhbgrUQ', registered_courses=[])
    ]

    actual = sort_by_courses_registered(students)
    assert len(actual) == len(expected)
    assert type(actual) == list

    for actual_student_obj, expected_student_obj in zip(actual, expected):
        assert actual_student_obj == expected_student_obj