# Calendar-Utils 📅

A tiny Python utility to calculate days in a month and check leap years.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Features
- ✅ Leap year detection (handles century rules correctly)
- ✅ Days in month calculation (February handled correctly)
- ✅ Input validation with proper errors
- ✅ Fully tested

## Installation
```bash
git clone https://github.com/tgangese/Calendar-Utils.git
cd Calendar-Utils
```

## Usage
```python
from calendar_utils import days_in_month, is_leap

print(days_in_month(2026, 2))  # 28
print(days_in_month(2024, 2))  # 29
print(is_leap(2024))           # True
print(is_leap(2026))           # False
```

Run as script:
```bash
python calendar_utils.py
```

## Run Tests
```bash
python -m unittest test_calendar.py -v
```

## How it works
- Leap year = divisible by 4, except centuries not divisible by 400.
- February has 29 days on leap years.

## License
MIT