# Import the module being tested
import pytest
from student import Student

# Test file location: tests/test_student_fix.py

def test_empty_grades_lowest():
    # Test that lowest() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.lowest() == 0

def test_empty_grades_highest():
    # Test that highest() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.highest() == 0

def test_empty_grades_average():
    # Test that average() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.average() == 0

def test_empty_grades_is_passing():
    # Test that is_passing() returns False when grades is empty
    s = Student("Ali", [])
    assert not s.is_passing()

def test_empty_grades_grade_letter():
    # Test that grade_letter() returns 'F' when grades is empty
    s = Student("Ali", [])
    assert s.grade_letter() == 'F'

def test_non_empty_grades_lowest():
    # Test that lowest() returns the correct value when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.lowest() == 70

def test_non_empty_grades_highest():
    # Test that highest() returns the correct value when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.highest() == 90

def test_non_empty_grades_average():
    # Test that average() returns the correct value when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.average() == 80.0

def test_non_empty_grades_is_passing():
    # Test that is_passing() returns the correct value when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.is_passing()

def test_non_empty_grades_grade_letter():
    # Test that grade_letter() returns the correct value when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.grade_letter() == 'B'