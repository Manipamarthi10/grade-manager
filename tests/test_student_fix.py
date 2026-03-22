# Import the module being tested
from student import Student

# Test file: tests/test_student_fix.py

def test_reproduce_bug():
    # Test that a student with exactly 40 points is incorrectly marked as not passing
    s = Student("Ali", [40])
    assert s.is_passing() == False  # This should fail

def test_verify_fix():
    # Test that a student with exactly 40 points is correctly marked as passing
    s = Student("Ali", [40])
    assert s.is_passing() == True  # This should pass

def test_edge_case_empty_grades():
    # Test that a student with no grades is correctly marked as not passing
    s = Student("Ali", [])
    assert s.is_passing() == False  # This should pass

def test_edge_case_single_grade():
    # Test that a student with a single grade is correctly marked as passing
    s = Student("Ali", [50])
    assert s.is_passing() == True  # This should pass

def test_edge_case_single_grade_below_passing():
    # Test that a student with a single grade below passing is correctly marked as not passing
    s = Student("Ali", [30])
    assert s.is_passing() == False  # This should pass