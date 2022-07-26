=============================
The ``0-add_integer`` module
=============================

Using ``add_integer``
---------------------

Import the function:

    >>> add_integer = __import__('0-add_integer').add_integer

Now test it:

    >>> add_integer(1, 2)
    3

    >>> add_integer(1, 9.3)
    10

    >>> add_integer(2)
    100

    >>> add_integer(3, -1)
    2

    >>> add_integer(-2, -1)
    -3

    >>> add_integer(10.0, 2.0)
    12

    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer()
    Traceback (most recent call last):
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer(1000e1000)
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

    >>> add_integer("Hello", "World")
    Traceback (most recent call last):
    TypeError: a must be an integer

    >>> add_integer(float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer
