class AVar:
    def __init__(self, val, der=0.0):
        self.val = val
        self.der = der 

    def __add__(self, other):
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(other.val + self.val, self.der + other.der)
    
    def __mul__(self, other):
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(other.val * self.val, self.val * other.der + self.der * other.val)
    
    def __truediv__(self, other):
        other = other if isinstance(other, AVar) else AVar(other)

        der = (other.val * self.der - self.val * other.der) / other.val**2

        return AVar(self.val / other.val, der)