import math 
import pytest

from ArithVar import AVar

def test_add():
    x = AVar(2.0, der=1.0)
    y = AVar(3.0, der=0.0)

    z = x + y 

    assert z.val == 5.0
    assert z.der == 1.0

def test_mult():
    x = AVar(2.0, der=3.0)
    y = AVar(3.0, der=4.0)

    z = x * y 

    assert z.val == 6.0
    assert z.der == 17.0

def test_div():
    x = AVar(2.0, der=3.0)
    y = AVar(3.0, der=4.0)

    z = x / y 
    # Standard divide between non-zero derivatives
    assert z.val == 2.0/3.0
    assert z.der == 1/9

    # Edge case where y == 0
    y = AVar(0.0, der=0.0)
    with pytest.raises(ZeroDivisionError):
        _ = x / y


def test_pow():
    x = AVar(2.0, der=1.0)
    y = AVar(3.0, der=1.0)

    z = x ** y

    assert z.val == 8 
    assert z.der == 12
    
    