import sys
from json import load

sys.path.append('./src')

from lab01 import *

def test_store_course_registrations_05():
    students = [ 
        Student(given_name='UcEki', surname='uYKVmjzXrI', registered_courses=[]), \
        Student(given_name='XopTMoflRk', surname='GgVjbhV', registered_courses=['CO310']), \
        Student(given_name='jED', surname='nigDsctTbU', registered_courses=['CO878', 'CO770', 'CO738', 'CO095']), \
        Student(given_name='kVgvzk', surname='tatt', registered_courses=['CO932', 'CO045', 'CO563', 'CO719', 'CO278']), \
        Student(given_name='OAQJ', surname='JwUKHANw', registered_courses=['CO023', 'CO742', 'CO278', 'CO758', 'CO971'])
    ]

    store_course_registrations(students, "Q4_output.json");
    with open("Q4_output.json", "r") as file:
        json_input = load(file)
    
    assert type(json_input) == list
    assert len(json_input) == len(students)
    actual = [Student(**x) for x in json_input]
    for actual_Obj, expected_Obj in zip(actual, students):
        assert actual_Obj == expected_Obj
