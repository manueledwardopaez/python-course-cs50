from twttr import shorten


def test_lowercase_vowels():
    assert shorten("hello") == "hll"


def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"


def test_both_case():
    assert shorten("Hello") == "Hll"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
