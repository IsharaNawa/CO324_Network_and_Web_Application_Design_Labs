#E/17/219

## NOTE: REMOVE THE pass STATEMENTS WHEN COMPLETING THE FUNCTIONS! ##
from dataclasses import dataclass, asdict
from json import dumps
from typing import List, Dict, IO, Tuple

@dataclass
class Student:
    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]


def load_course_registrations(filename: str) -> List[Student]:
    """ Returns a list of Student objects read from filename"""
    with open(filename, 'r') as file:
        filecontent = file.read()
        studentdetails = filecontent.split("\n")
        studentdetails.remove("")

    file.close()

    StudentList = []

    for student in studentdetails:
        details=student.split(",")
        newstudent = Student(details[0],details[1],details[2:])
        StudentList.append(newstudent)

    return StudentList

#StudentList = load_course_registrations("../student_registrations.csv")
   
def sort_by_courses_registered(students: List[Student]) -> List[Student]:
    """Sort students by the number of courses that they are registered for"""

    students = sorted(students,key = lambda student: len(student.registered_courses),reverse = True)

    return students

#StudentList = sort_by_courses_registered(StudentList)
#print(StudentList)

def index_by_name(students: List[Student]) -> Dict[Tuple, Student]:
    """Store Students keyed by (surname, given_name) in a dictionary"""
    StudentDict = {}

    for student in students:
        key = (student.surname,student.given_name)
        StudentDict[key] = student 

    return StudentDict

#s = index_by_name(StudentList)
#print(s)

def store_course_registrations(students: List[Student], filename:str):
    """Writes a list of Student to a file"""
    with open(filename, 'w') as file:
         jsonStd = dumps(list(map(asdict , students)))
         file.write(jsonStd)

    file.close()

# # Might be useful to test locally
# if __name__ == "__main__":
#     # Your Code to test locally.
