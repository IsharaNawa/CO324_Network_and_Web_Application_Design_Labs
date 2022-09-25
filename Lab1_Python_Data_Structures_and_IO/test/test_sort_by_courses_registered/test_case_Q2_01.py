import sys

sys.path.append('./src')

from lab01 import *

def test_sort_by_courses_registered_01():
    students = [ 
        Student(given_name='RBsxIDEnk', surname='VEHEtIX', registered_courses=['CO552', 'CO771']), \
        Student(given_name='AhaGdX', surname='nnxlK', registered_courses=['CO688', 'CO806', 'CO842', 'CO624']), \
        Student(given_name='cIGYd', surname='zDOESpDXT', registered_courses=['CO732', 'CO596']), \
        Student(given_name='IctCZDzhUz', surname='gFoBWlbs', registered_courses=['CO706']), \
        Student(given_name='MxcOPiew', surname='OvitvYSEI', registered_courses=['CO032', 'CO616', 'CO491', 'CO824', 'CO603']), \
        Student(given_name='VZgUWb', surname='ULbQMa', registered_courses=[])
    ]

    expected = [
        Student(given_name='MxcOPiew', surname='OvitvYSEI', registered_courses=['CO032', 'CO616', 'CO491', 'CO824', 'CO603']), \
        Student(given_name='AhaGdX', surname='nnxlK', registered_courses=['CO688', 'CO806', 'CO842', 'CO624']), \
        Student(given_name='RBsxIDEnk', surname='VEHEtIX', registered_courses=['CO552', 'CO771']), \
        Student(given_name='cIGYd', surname='zDOESpDXT', registered_courses=['CO732', 'CO596']), \
        Student(given_name='IctCZDzhUz', surname='gFoBWlbs', registered_courses=['CO706']), \
        Student(given_name='VZgUWb', surname='ULbQMa', registered_courses=[])
    ]

    actual = sort_by_courses_registered(students)
    assert len(actual) == len(expected)
    assert type(actual) == list

    for actual_student_obj, expected_student_obj in zip(actual, expected):
        assert actual_student_obj == expected_student_obj