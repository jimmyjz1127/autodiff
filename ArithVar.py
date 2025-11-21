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