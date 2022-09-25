import sys

sys.path.append('./src')

from lab01 import *

def test_index_by_name_04():
    students = [ 
        Student(given_name='eAgKpa', surname='LXOe', registered_courses=['CO513']), \
        Student(given_name='ClMbY', surname='rIfT', registered_courses=['CO431', 'CO008', 'CO006', 'CO655']), \
        Student(given_name='sARiPP', surname='DhBjXXR', registered_courses=['CO902', 'CO501', 'CO142', 'CO899', 'CO068']), \
        Student(given_name='Mkj', surname='Vdh', registered_courses=[]), \
        Student(given_name='MTMaLqrBvz', surname='HFpuolfB', registered_courses=[]), \
        Student(given_name='gqIBBei', surname='iKuBa', registered_courses=['CO489']), \
        Student(given_name='ZpbZRTxxt', surname='yRYkWavo', registered_courses=[]), \
        Student(given_name='YmLa', surname='LrFDWAdM', registered_courses=['CO497', 'CO600', 'CO906', 'CO479'])
    ]

    actual = index_by_name(students)
    assert len(actual) == len(students)
    assert type(actual) == dict

    for student in students:
        assert actual[(student.surname, student.given_name)] == student
        assert all([type(key) == tuple for key in actual.keys()])
        assert all([type(actual[key]) == Student for key in actual.keys()])