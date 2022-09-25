import sys
from json import load

sys.path.append('./src')

from lab01 import *

def test_store_course_registrations_01():
    students = [ 
        Student(given_name='baszWQxH', surname='yYxrEP', registered_courses=['CO017', 'CO591', 'CO662', 'CO863', 'CO546']), \
        Student(given_name='fRoTr', surname='GUlj', registered_courses=['CO139', 'CO138', 'CO957']), \
        Student(given_name='rlOugmncT', surname='lRxfmZ', registered_courses=['CO505', 'CO980', 'CO398', 'CO846']), \
        Student(given_name='VZCBDRmun', surname='wNG', registered_courses=['CO453', 'CO878']), \
        Student(given_name='JzN', surname='tMvSwsVYNx', registered_courses=['CO293', 'CO480', 'CO425', 'CO953', 'CO283']), \
        Student(given_name='sufub', surname='UtYY', registered_courses=[]), \
        Student(given_name='lbGhImbu', surname='qYOZMsY', registered_courses=['CO175']), \
        Student(given_name='dYd', surname='HwDOyMCIZq', registered_courses=['CO955', 'CO699']), \
        Student(given_name='wBIOacetXS', surname='DpoWNQaKl', registered_courses=['CO831', 'CO191', 'CO500', 'CO693', 'CO858']), \
        Student(given_name='Ieq', surname='dAkg', registered_courses=['CO024', 'CO234'])
    ]

    store_course_registrations(students, "Q4_output.json");
    with open("Q4_output.json", "r") as file:
        json_input = load(file)
    
    assert type(json_input) == list
    assert len(json_input) == len(students)
    actual = [Student(**x) for x in json_input]
    for actual_Obj, expected_Obj in zip(actual, students):
        assert actual_Obj == expected_Obj
