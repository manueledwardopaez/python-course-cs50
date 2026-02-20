from hello import hello

def test_deafult():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Ron", "Harry"]:
        assert hello(name) == f"hello, {name}"
