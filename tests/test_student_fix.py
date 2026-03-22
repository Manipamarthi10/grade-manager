# Import the module being tested
from student import Student

# Test file location: tests/test_student_fix.py

def test_empty_grades_lowest():
    # Test that the lowest() method returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.lowest() == 0  # FAILS: ValueError

def test_empty_grades_lowest_fixed():
    # Test that the lowest() method returns 0 when grades is empty (fixed)
    s = Student("Ali", [])
    assert s.lowest() == 0  # Should pass

def test_empty_grades_average():
    # Test that the average() method returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.average() == 0  # Should pass

def test_empty_grades_highest():
    # Test that the highest() method returns 0 when grades is empty
    s = Student("Ali", [])
    assert s.highest() == 0  # Should pass

def test_empty_grades_is_passing():
    # Test that the is_passing() method returns False when grades is empty
    s = Student("Ali", [])
    assert not s.is_passing()  # Should pass

def test_empty_grades_grade_letter():
    # Test that the grade_letter() method returns 'F' when grades is empty
    s = Student("Ali", [])
    assert s.grade_letter() == 'F'  # Should pass