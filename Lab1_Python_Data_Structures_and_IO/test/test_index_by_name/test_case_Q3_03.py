import sys

sys.path.append('./src')

from lab01 import *

def test_index_by_name_03():
    students = [ 
        Student(given_name='qoq', surname='mLHjd', registered_courses=['CO388', 'CO415', 'CO010', 'CO037']), \
        Student(given_name='GvIk', surname='hzFkaikr', registered_courses=['CO850']), \
        Student(given_name='AiLVOTdfw', surname='NJf', registered_courses=['CO339', 'CO061', 'CO621']), \
        Student(given_name='GepcybgO', surname='GOUCzP', registered_courses=['CO140', 'CO813', 'CO195']), \
        Student(given_name='QvxIVTDCZI', surname='KyUvuaLMKC', registered_courses=['CO992', 'CO893'])
    ]

    actual = index_by_name(students)
    assert len(actual) == len(students)
    assert type(actual) == dict

    for student in students:
        assert actual[(student.surname, student.given_name)] == student
        assert all([type(key) == tuple for key in actual.keys()])
        assert all([type(actual[key]) == Student for key in actual.keys()])