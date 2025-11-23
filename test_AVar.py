import math 
import pytest
import numpy as np

from ArithVar import AVar, sin, cos, tan, log, exp

"""
    ##############################################
    ############ Aithmetic Operations ############
    ##############################################
"""
def test_add():
    x = AVar(2.0, der=1.0)
    y = AVar(3.0, der=0.0)

    z = x + y 

    assert z.val == 5.0
    assert z.der == 1.0

def test_sub():
    x = AVar(2.0, der=2.0)
    y = AVar(3.0, der=1.0)

    z = x - y

    assert z.val == -1.0
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

"""
    ###############################################
    ########## Non-Arithmetic Operations ##########
    ###############################################
"""

def test_pow():
    x = AVar(2.0, der=1.0)
    y = AVar(3.0, der=0.0)

    z = x ** y

    assert z.val == 8 
    assert z.der == 12

    # x ^ g(x)
    c = AVar(2.0, der=0.0)
    z = x ** (c * x)

    assert z.val == 16
    assert z.der == 16 * (2 * math.log(2) + 2)
    
    
def test_sin():
    x = AVar(math.pi, der=1.0)
    z = sin(x)

    assert z.val == math.sin(math.pi)
    assert z.der == -1

    x = AVar(math.pi / 4, der=1.0)
    z = sin(x)

    assert z.val == math.sin(math.pi / 4)
    assert z.der == math.cos(math.pi / 4)

def test_cos():
    x = AVar(math.pi, der=1.0)
    z = cos(x)

    assert z.val == -1
    assert z.der == -math.sin(math.pi)

    x = AVar(math.pi / 4, der=1.0)
    z = cos(x)

    assert z.val == math.cos(math.pi / 4)
    assert z.der == -math.sin(math.pi / 4)

def test_tan():
    x = AVar(math.pi/6, der=1.0)
    z = tan(x)

    assert z.val == math.tan(math.pi/6)
    assert z.der == (1/math.cos(math.pi/6))**2


def test_log():
    x = AVar(8, 1)
    z = log(x)

    assert z.val == math.log(8)
    assert z.der == x.der / x.val


def test_exp():
    x = AVar(3, 1.0)
    z = exp(x)

    assert z.val == math.exp(3)
    assert z.der == math.exp(3)

    c = AVar(3.0, 0.0)
    z = exp(x ** c)

    assert z.val == math.exp(27)
    assert z.der == (3 * 3 ** 2) * math.exp(27)
