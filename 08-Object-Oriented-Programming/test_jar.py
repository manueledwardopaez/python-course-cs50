import pytest
from jar import Jar
from unittest.mock import MagicMock


def test_init():
    jar = Jar()
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar("2")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.deposit("20")

def test_withdraw():
    jar = Jar(12)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(20) 
    with pytest.raises(ValueError):
        jar.withdraw(-5) 