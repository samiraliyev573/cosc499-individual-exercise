from helper import print_ascending, print_descending

# testing ascending
def test_ascending_zero():
    output = print_ascending(0)
    assert output == """"""

def test_ascending_one():
    output = print_ascending(1)
    assert output == """*\n"""

def test_ascending_two():
    output = print_ascending(2)
    assert output == """ *\n***\n"""

def test_ascending_three():
    output = print_ascending(3)
    assert output == """  *\n ***\n*****\n"""


# testing descending
def test_descending_zero():
    output = print_descending(0)
    assert output == """"""

def test_descending_one():
    output = print_descending(1)
    assert output == """*\n"""

def test_descending_three():
    output = print_descending(3)
    assert output == """*****\n ***\n  *\n"""