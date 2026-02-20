import pytest
from fuel import convert, gauge

def test_convert_Normal_case():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_convert_case_rounding():
    assert convert("2/3") == 67
    assert convert("1/3") == 33


def test_convert_case_limits():
    assert convert("1/1") == 100
    assert convert("0/1") == 0




def test_convert_error():
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("1/2.5")
    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_gauge_ful():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_perc():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(50) == "50%"

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
