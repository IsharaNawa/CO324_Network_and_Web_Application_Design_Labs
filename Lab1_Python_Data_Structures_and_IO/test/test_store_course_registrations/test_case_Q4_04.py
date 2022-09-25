import sys
from json import load

sys.path.append('./src')

from lab01 import *

def test_store_course_registrations_04():
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

    store_course_registrations(students, "Q4_output.json");
    with open("Q4_output.json", "r") as file:
        json_input = load(file)
    
    assert type(json_input) == list
    assert len(json_input) == len(students)
    actual = [Student(**x) for x in json_input]
    for actual_Obj, expected_Obj in zip(actual, students):
        assert actual_Obj == expected_Obj
