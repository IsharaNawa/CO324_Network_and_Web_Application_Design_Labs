import sys
from json import load

sys.path.append('./src')

from lab01 import *

def test_store_course_registrations_03():
    students = [ 
        Student(given_name='yzrV', surname='xBrWiMQbB', registered_courses=['CO821', 'CO555', 'CO118', 'CO759']), \
        Student(given_name='QOGQZF', surname='TWC', registered_courses=['CO512', 'CO684', 'CO168', 'CO997']), \
        Student(given_name='gwaqBYNkm', surname='HRSBj', registered_courses=['CO861', 'CO668', 'CO149', 'CO600', 'CO995']), \
        Student(given_name='yaNOJa', surname='inufVXAnQW', registered_courses=['CO995', 'CO154', 'CO160', 'CO193']), \
        Student(given_name='IvBTygO', surname='FNbtFhEme', registered_courses=['CO279', 'CO341', 'CO708', 'CO784', 'CO180']), \
        Student(given_name='ftFeC', surname='XtAyYXUn', registered_courses=[]), \
        Student(given_name='KkKytup', surname='Upt', registered_courses=['CO964', 'CO231', 'CO619', 'CO014', 'CO663']), \
        Student(given_name='wLOsde', surname='KrPq', registered_courses=['CO098', 'CO378']), \
        Student(given_name='gXCp', surname='VMgn', registered_courses=['CO033', 'CO280', 'CO099', 'CO988', 'CO967'])
    ]

    store_course_registrations(students, "Q4_output.json");
    with open("Q4_output.json", "r") as file:
        json_input = load(file)
    
    assert type(json_input) == list
    assert len(json_input) == len(students)
    actual = [Student(**x) for x in json_input]
    for actual_Obj, expected_Obj in zip(actual, students):
        assert actual_Obj == expected_Obj
