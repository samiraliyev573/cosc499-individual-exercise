from helper import print_ascending


def test_ascending_zero():
    output = print_ascending(0)
    assert output == """"""

def test_ascending_one():
    output = print_ascending(1)
    assert output == """*\n"""

def test_ascending_two():
    output = print_ascending(2)
    assert output == """ *\n***\n"""