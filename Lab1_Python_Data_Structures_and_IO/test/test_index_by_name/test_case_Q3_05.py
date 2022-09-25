import sys

sys.path.append('./src')

from lab01 import *

def test_index_by_name_05():
    students = [ 
        Student(given_name='BSbMzakmT', surname='IVlFrWFi', registered_courses=['CO706', 'CO799', 'CO823', 'CO837', 'CO360']), \
        Student(given_name='FNL', surname='kbrO', registered_courses=[]), \
        Student(given_name='tSYgUkInq', surname='Fwn', registered_courses=['CO947', 'CO659', 'CO058', 'CO962', 'CO682']), \
        Student(given_name='DzmLAr', surname='yUYSWdj', registered_courses=['CO300', 'CO179', 'CO338']), \
        Student(given_name='jjiPXD', surname='uAcYAhQg', registered_courses=['CO866', 'CO203']), \
        Student(given_name='eBuPosKlGM', surname='wcrbLL', registered_courses=['CO365', 'CO182', 'CO079', 'CO968', 'CO883']), \
        Student(given_name='USmlfcptM', surname='NNGqXf', registered_courses=['CO426']), \
        Student(given_name='KoBi', surname='jjHLs', registered_courses=['CO554', 'CO008', 'CO664', 'CO637']), \
        Student(given_name='sLlGXn', surname='ZhPZRZX', registered_courses=['CO508', 'CO817']), \
        Student(given_name='kXWDQezP', surname='aQlbElbEVo', registered_courses=['CO938', 'CO677', 'CO655'])
    ]

    actual = index_by_name(students)
    assert len(actual) == len(students)
    assert type(actual) == dict

    for student in students:
        assert actual[(student.surname, student.given_name)] == student
        assert all([type(key) == tuple for key in actual.keys()])
        assert all([type(actual[key]) == Student for key in actual.keys()])