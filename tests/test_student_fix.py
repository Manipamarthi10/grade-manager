# Import the module being tested
from student import Student

# Test file location: tests/test_student_fix.py

def test_empty_grades_highest():
    # Test that highest() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.highest() == 0

def test_empty_grades_average():
    # Test that average() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.average() == 0

def test_empty_grades_lowest():
    # Test that lowest() returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.lowest() == 0

def test_empty_grades_is_passing():
    # Test that is_passing() returns False when average is exactly 40
    s = Student("Ali", [])
    assert s.is_passing() == False

def test_non_empty_grades_highest():
    # Test that highest() returns the highest grade when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.highest() == 90

def test_non_empty_grades_average():
    # Test that average() returns the average of grades when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.average() == 80.0

def test_non_empty_grades_lowest():
    # Test that lowest() returns the lowest grade when grades is not empty
    s = Student("Ali", [90, 80, 70])
    assert s.lowest() == 70

def test_non_empty_grades_is_passing():
    # Test that is_passing() returns True when average is greater than 40
    s = Student("Ali", [90, 80, 70])
    assert s.is_passing() == True