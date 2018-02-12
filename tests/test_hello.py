import hello

"""
Tests the hello module
"""


def test_hello_no_name():
    """
    Checks that if no name passed we get hello, world
    """

    assert hello.hello() == 'Hello, World'


def test_hello_with_name():
    """
    If passed a name returns, "Hello, name"
    """

    assert hello.hello('Olly') == 'Hello, Olly'
