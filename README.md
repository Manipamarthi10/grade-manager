# Grade Manager

A Python student grade management system.

## Files

- `student.py` — Student class with grade calculations
- `manager.py` — GradeManager class to manage multiple students
- `tests/test_grades.py` — Test suite

## Run Tests

```bash
pip install pytest
pytest tests/ -v
```

## Usage

```python
from manager import GradeManager

m = GradeManager()
m.add_student("Ali", [85, 90, 78])
print(m.top_student().name)     # Ali
print(m.class_average())        # 84.33
```
