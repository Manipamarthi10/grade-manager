# Import the module being tested
from student import Student

# Test file location: tests/test_student_fix.py

def test_empty_grades_average():
    # Test that average of empty grades returns 0
    s = Student("Ali", [])
    assert s.average() == 0

def test_empty_grades_average_fix():
    # Test that average of empty grades returns 0 after fix
    s = Student("Ali", [])
    assert s.average() == 0

def test_empty_grades_highest():
    # Test that highest of empty grades returns 0
    s = Student("Ali", [])
    assert s.highest() == 0

def test_empty_grades_lowest():
    # Test that lowest of empty grades returns 0
    s = Student("Ali", [])
    assert s.lowest() == 0

def test_empty_grades_is_passing():
    # Test that is_passing of empty grades returns False
    s = Student("Ali", [])
    assert s.is_passing() == False

def test_non_empty_grades_average():
    # Test that average of non-empty grades returns correct value
    s = Student("Ali", [90, 80, 70])
    assert s.average() == 80

def test_non_empty_grades_highest():
    # Test that highest of non-empty grades returns correct value
    s = Student("Ali", [90, 80, 70])
    assert s.highest() == 90

def test_non_empty_grades_lowest():
    # Test that lowest of non-empty grades returns correct value
    s = Student("Ali", [90, 80, 70])
    assert s.lowest() == 70

def test_non_empty_grades_is_passing():
    # Test that is_passing of non-empty grades returns correct value
    s = Student("Ali", [90, 80, 70])
    assert s.is_passing() == True