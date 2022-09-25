import sys
from json import load

sys.path.append('./src')

from lab01 import *

def test_store_course_registrations_02():
    students = [ 
        Student(given_name='lvwmN', surname='dmQ', registered_courses=['CO086']), \
        Student(given_name='OcA', surname='sPOAWMHLqF', registered_courses=['CO000', 'CO172', 'CO313']), \
        Student(given_name='PfURfBo', surname='iVSn', registered_courses=['CO977', 'CO279', 'CO549', 'CO427']), \
        Student(given_name='uVzm', surname='SENjfNM', registered_courses=['CO141']), \
        Student(given_name='pHozY', surname='hugVGi', registered_courses=['CO671', 'CO280'])
    ]

    store_course_registrations(students, "Q4_output.json");
    with open("Q4_output.json", "r") as file:
        json_input = load(file)
    
    assert type(json_input) == list
    assert len(json_input) == len(students)
    actual = [Student(**x) for x in json_input]
    for actual_Obj, expected_Obj in zip(actual, students):
        assert actual_Obj == expected_Obj
