from bank import value


def test_hello():
    assert value("hello") == 0


def test_case_insensitivity():
    assert value("Hello") == 0


def test_full_phrase():
    assert value("Hello, Newman") == 0


def test_h_but_not_hello():
    assert value("Hi") == 20


def test_other():
    assert value("Good morning") == 100
