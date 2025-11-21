import math
import numpy as np

class AVar:
    def __init__(self, val, der=0.0):
        '''
            Constructor 
        '''
        self.val = val
        self.der = der 

    def __add__(self, other):
        '''
            Add operation
        '''
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(other.val + self.val, self.der + other.der)
    
    def __mul__(self, other):
        ''' 
            Multiplication operation
        '''
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(other.val * self.val, self.val * other.der + self.der * other.val)
    
    def __truediv__(self, other):
        '''
            Division operation
        '''

        other = other if isinstance(other, AVar) else AVar(other)

        der = (other.val * self.der - self.val * other.der) / other.val**2

        return AVar(self.val / other.val, der)
    
    def __pow__(self, other):
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(self.val ** other.val, other.val * (self.val ** (other.val - 1)) * self.der)
    
''' 
    #################################################
    ################ Trig Functions #################
    #################################################
'''
def sin(x):
    if isinstance(x, AVar):
        return AVar(
            math.sin(x.val),
            math.cos(x.val) * x.der
        )

    return math.sin(x)

def cos(x):
    if isinstance(x, AVar):
        return AVar(
            math.cos(x.val),
            -math.sin(x.val) * x.der
        )
    return math.cos(x)


def tan(x):
    if isinstance(x, AVar):
        val = math.tan(x.val)
        der = (1.0 + val * val) * x.der
        return AVar(val, der)
    return math.tan(x)

"""
    ########################################
    ########## Utility Functions ###########
    ########################################
"""
def log(x):
    if isinstance(x, AVar):
        val = math.log(x.val)
        der = x.der * 1.0/val
        return AVar(val, der)
    return math.log(x)

"""
    ########################################
    ########## Utility Functions ###########
    ########################################
"""
