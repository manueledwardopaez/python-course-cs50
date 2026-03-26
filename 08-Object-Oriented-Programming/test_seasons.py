import pytest
from seasons import seasons
from datetime import date

def test_seasons_correct():
    DOB     = date(2025, 3, 23)
    today   = date(2026, 3, 23)
    assert seasons(today, DOB) == "Five hundred twenty-five thousand, six hundred minutes"

def test_seasons_leap_year():
    DOB     = date(1999, 3, 23)
    today   = date(2000, 3, 23)
    assert seasons(today, DOB) == "Five hundred twenty-seven thousand forty minutes"

def test_seasons_invalid_input():
    with pytest.raises(AttributeError):
        seasons(2025, 2026)
