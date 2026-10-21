# Calendar Utils
A tiny Python utility to calculate days in a month and check leap years.

## Features
- Leap year detection
- Days in month calculation (handles February correctly)
- Input validation

## Usage
from calendar_utils import days_in_month, is_leap

print(days_in_month(2026, 2)) # 28
print(is_leap(2024)) # True

## Run Tests
python -m unittest test_calendar.py