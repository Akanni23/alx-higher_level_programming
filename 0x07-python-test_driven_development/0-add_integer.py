#!/usr/bin/python3

"""Defines an integer addition function."""

def add_integer(a, =98):
    """Return the integer addition of a and b.
    Float arguments are typycasted to ints before addition is performed.
    Raises:
    TypeError: If either of a or b is a non - integer and non - float.
    """
    
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        rise TypeError("b must be an integer")
        return (int(a) + int(b))
