import sys
from random import randint, choices
from string import ascii_letters, digits
from typing import List
from json import dumps
from dataclasses import asdict

sys.path.append('./src')

from lab01 import *


def generate_user_data(filename:str) -> List[str]:
    no_of_users = randint(5, 10)
    data = []
    students = []
    for i in range(no_of_users):
        given_name = "".join(choices(ascii_letters, k = randint(3, 10)))
        surname = "".join(choices(ascii_letters, k = randint(3, 10)))
        courses = ",".join(["CO" + "".join(choices(digits, k = 3)) for _ in range(randint(0, 5))])
        if courses != "":
            data.append(given_name + "," + surname + "," + courses)
            students.append(Student(given_name, surname, courses.split(',')))
        else:
            data.append(given_name + "," + surname)
            students.append(Student(given_name, surname, []))

    with open(filename, "w") as file:
        for user in data:
            file.write(user + "\n")
    return students


def test_load_course_registrations():
    for i in range(5):
        expected = generate_user_data("input.csv")
        actual = load_course_registrations("input.csv")
        assert type(actual) == list
        assert len(actual) == len(expected)
        for actualStudent, expectedStudent in zip(actual, expected):
            assert actualStudent == expectedStudent