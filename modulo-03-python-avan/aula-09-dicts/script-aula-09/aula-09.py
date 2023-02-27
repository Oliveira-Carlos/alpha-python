from typing import Dict


student_name = input("enter the name of the student")

while True:
    student_grade = float(
        input("enter the grade of the student between 0 and 10"))
    if student_grade >= 0 and student_grade <= 10:
        break


def passed_or_failed(grade: float) -> str:
    """
    This function takes a grade as input and returns "passed" if the grade is
    greater than or equal to 7 and "failed" otherwise.
    """

    if grade >= 7:
        return "passed"

    return "failed"


def show_dict(dict: Dict) -> None:
    """
    Prints the dictionary content to the standard output.
    """

    print(f"dictionary content:{dict}")


student_dict = {
    "name": student_name,
    "grade": student_grade,
    "result": passed_or_failed(student_grade)
}

show_dict(student_dict)
