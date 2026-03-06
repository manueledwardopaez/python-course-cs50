from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True


def test_invalid_range():
    assert validate("256.100.100.100") == False
    assert validate("192.168.1.300") == False
    assert validate("999.999.999.999") == False


def test_invalid_format():
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("hello.world") == False
    assert validate("192.168.01.1") == False