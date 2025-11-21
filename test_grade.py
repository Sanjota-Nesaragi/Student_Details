import pytest
from grade import get_student_details, calculate_grade


def test_get_student_details():
    student = get_student_details("Sanjota", "CSE", 3, 85, 90, 88)

    assert student["name"] == "Sanjota"
    assert student["department"] == "CSE"
    assert student["semester"] == 3
    assert student["marks"] == [85, 90, 88]


def test_calculate_grade_S():
    avg, grade = calculate_grade([95, 92, 90])
    assert round(avg, 2) == 92.33
    assert grade == "S"


def test_calculate_grade_A():
    avg, grade = calculate_grade([80, 85, 82])
    assert grade == "A"


def test_calculate_grade_B():
    avg, grade = calculate_grade([70, 75, 72])
    assert grade == "B"


def test_calculate_grade_C():
    avg, grade = calculate_grade([50, 60, 55])
    assert grade == "C"


def test_calculate_grade_D():
    avg, grade = calculate_grade([40, 45, 48])
    assert grade == "D"


def test_calculate_grade_F():
    avg, grade = calculate_grade([10, 30, 25])
    assert grade == "F"