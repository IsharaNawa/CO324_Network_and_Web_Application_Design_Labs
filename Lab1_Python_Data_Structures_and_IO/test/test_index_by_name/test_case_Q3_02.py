import sys

sys.path.append('./src')

from lab01 import *

def test_index_by_name_02():
    students = [ 
        Student(given_name='yNZdUrfSa', surname='aevMOe', registered_courses=['CO634', 'CO920', 'CO664', 'CO894', 'CO566']), \
        Student(given_name='AfOkgL', surname='SZZfpvWlhz', registered_courses=['CO685', 'CO180', 'CO015', 'CO954', 'CO304']), \
        Student(given_name='jYqUvs', surname='TAJpO', registered_courses=['CO765', 'CO483', 'CO884']), \
        Student(given_name='CohXAThjLR', surname='DTsqX', registered_courses=[]), \
        Student(given_name='nUypzrgCe', surname='cPfqF', registered_courses=['CO127', 'CO550', 'CO076', 'CO275']), \
        Student(given_name='sMGBmh', surname='bTpbugwllo', registered_courses=[]), \
        Student(given_name='XRi', surname='UlpnObrSg', registered_courses=['CO926', 'CO959', 'CO444', 'CO473'])
    ]

    actual = index_by_name(students)
    assert len(actual) == len(students)
    assert type(actual) == dict

    for student in students:
        assert actual[(student.surname, student.given_name)] == student
        assert all([type(key) == tuple for key in actual.keys()])
        assert all([type(actual[key]) == Student for key in actual.keys()])