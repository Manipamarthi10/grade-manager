import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student
from manager import GradeManager


def test_average_normal():
    """Normal average calculation should work correctly."""
    s = Student("Ali", [80, 90, 70])
    assert s.average() == 80.0


def test_empty_grades_average():
    """Average of empty grades should return 0, not crash."""
    s = Student("Ali", [])
    assert s.average() == 0  # FAILS: ZeroDivisionError


def test_empty_grades_highest():
    """Highest of empty grades should return 0, not crash."""
    s = Student("Ali", [])
    assert s.highest() == 0  # FAILS: ValueError


def test_empty_grades_lowest():
    """Lowest of empty grades should return 0, not crash."""
    s = Student("Ali", [])
    assert s.lowest() == 0  # FAILS: ValueError


def test_is_passing_boundary():
    """A student with exactly 40 should be passing."""
    s = Student("Ali", [40])
    assert s.is_passing() == True  # FAILS: 40 > 40 is False


def test_is_passing_above():
    """A student above 40 should be passing."""
    s = Student("Ali", [80])
    assert s.is_passing() == True  # PASSES


def test_is_failing_below():
    """A student below 40 should be failing."""
    s = Student("Ali", [30])
    assert s.is_passing() == False  # PASSES


def test_grade_letter_A():
    """Student with 95 average should get A."""
    s = Student("Ali", [95, 95])
    assert s.grade_letter() == "A"  # PASSES


def test_grade_letter_F():
    """Student with 30 average should get F."""
    s = Student("Ali", [30, 30])
    assert s.grade_letter() == "F"  # PASSES


def test_get_missing_student():
    """Getting a non-existent student should return None, not crash."""
    m = GradeManager()
    result = m.get_student("Nobody")
    assert result is None  # FAILS: KeyError


def test_class_average_empty():
    """Class average with no students should return 0, not crash."""
    m = GradeManager()
    assert m.class_average() == 0  # FAILS: ZeroDivisionError


def test_class_average_normal():
    """Class average with students should calculate correctly."""
    m = GradeManager()
    m.add_student("Ali", [80, 90])
    m.add_student("Sara", [60, 70])
    assert m.class_average() == 75.0  # PASSES


def test_top_student_normal():
    """Top student should be the one with highest average."""
    m = GradeManager()
    m.add_student("Ali", [90, 85])
    m.add_student("Sara", [70, 75])
    assert m.top_student().name == "Ali"  # PASSES


def test_top_student_empty():
    """Top student with no students should return None, not crash."""
    m = GradeManager()
    assert m.top_student() is None  # FAILS: ValueError


def test_add_grade_missing_student():
    """Adding grade to non-existent student should raise ValueError, not KeyError."""
    m = GradeManager()
    try:
        m.add_grade("Nobody", 80)
        assert False, "Should have raised an error"
    except ValueError:
        pass  # FAILS: raises KeyError instead of ValueError


def test_failing_students():
    """Failing students list should be accurate."""
    m = GradeManager()
    m.add_student("Ali", [80])
    m.add_student("Sara", [30])
    assert m.failing_students() == ["Sara"]  # PASSES
