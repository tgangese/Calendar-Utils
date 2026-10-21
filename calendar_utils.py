"""
calendar_utils.py
A simple utility to work with calendar dates.
"""

from typing import List

# Index 0 is placeholder so month number == list index
MONTH_DAYS: List[int] = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NAMES: List[str] = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def is_leap(year: int) -> bool:
    """
    Determine if a year is a leap year.

    Args:
        year: The year to check (e.g., 2026)

    Returns:
        True if leap year, False otherwise.
    
    Leap year rule: Divisible by 4, except centuries not divisible by 400.
    """
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """
    Return number of days in a given month and year.

    Args:
        year: Year as integer
        month: Month as integer (1-12)

    Returns:
        Number of days in that month.

    Raises:
        ValueError: If month is not in 1-12
    """
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}. Month must be between 1 and 12.")

    if month == 2 and is_leap(year):
        return 29

    return MONTH_DAYS[month]

def get_month_name(month: int) -> str:
    """Return month name for a given month number."""
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}")
    return MONTH_NAMES[month]

if __name__ == "__main__":
    # Simple demo / CLI
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        print(f"{get_month_name(month)} {year} has {days_in_month(year, month)} days.")
        print(f"Is {year} a leap year? {is_leap(year)}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")