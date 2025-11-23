import math
import numpy as np
from graphviz import Digraph

# types = {const, add, mul, div, pow, log, sin, cos, tan}

class AVar:
    def __init__(self, val, der=0.0, parents=(), op='const'):
        '''
            Constructor 
        '''
        self.val = val
        self.der = der 
        self.parents = parents
        self.op = op

    def __add__(self, other):
        '''
            Add operation
        '''
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(
                        self.val + other.val, 
                        self.der + other.der, 
                        parents=(self,other), 
                        op='sub'
                    )
    
    def __sub__(self, other):
        '''
            Subtraction operation
        '''
        other = other if isinstance(other, AVar) else AVar(other)

        return AVar(
                        self.val - other.val, 
                        self.der - other.der, 
                        parents=(self,other), 
                        op='add'
                    )

    
    def __mul__(self, other):
        ''' 
            Multiplication operation
        '''
        other = other if isinstance(other, AVar) else AVar(other)
        return AVar(
                        other.val * self.val, 
                        self.val * other.der + self.der * other.val, 
                        parents=(self,other), 
                        op='mul'
                    )
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        '''
            Division operation
        '''

        other = other if isinstance(other, AVar) else AVar(other)
        der = (other.val * self.der - self.val * other.der) / other.val**2
        return AVar(self.val / other.val, der, parents=(self,other), op='div')
    
    def __pow__(self, other):
        other = other if isinstance(other, AVar) else AVar(other)

        u = self
        v = other

        # value
        val = u.val ** v.val

        # derivative: (u^v)(v' ln(u) + v u'/u)
        der = val * (v.der * math.log(u.val) + v.val * (u.der / u.val))

        return AVar(val, der, parents=(u, v), op="pow")
    
''' 
    #################################################
    ################ Trig Functions #################
    #################################################
'''
def sin(x):
    if isinstance(x, AVar):
        return AVar(
            math.sin(x.val),
            math.cos(x.val) * x.der,
            parents = [x],
            op='sin'
        )

    return math.sin(x)

def cos(x):
    if isinstance(x, AVar):
        return AVar(
            math.cos(x.val),
            -math.sin(x.val) * x.der,
            parents=[x],
            op='cos'
        )
    return math.cos(x)


def tan(x):
    if isinstance(x, AVar):
        val = math.tan(x.val)
        der = (1.0 + val * val) * x.der
        return AVar(val, der, parents=(x,), op='tan')
    return math.tan(x)

"""
    ########################################
    ########## Other Functions ###########
    ########################################
"""
def log(x):
    if isinstance(x, AVar):
        val = math.log(x.val)
        der = x.der / x.val
        return AVar(val, der, parents=[x], op='log')
    return math.log(x)

"""
    ########################################
    ########## Utility Functions ###########
    ########################################
"""
def trace(root):
    nodes = []
    stack = [root] 

    while stack:
        node = stack.pop() 
        nodes.append(node)
        for parent in node.parents:
            stack.append(parent)

    return nodes

op_dict = {
    "add":"+",
    "sub":"-",
    "mul":"*",
    "div":"/",
    "pow":"^",
    "sin":"sin(.)",
    "cos":"cos(.)",
    "tan":"tan(.)"
}


def draw_graph(root):
    dot = Digraph()
    nodes = trace(root)

    for i,n in enumerate(nodes):
        name=f"n{n.val}{n.op} "
        label=op_dict[n.op] if n.op != "const" else f"{n.val}"
        dot.node(name, label)
        n._dot_name = name 

    for n in nodes:
        for p in n.parents:
            dot.edge(p._dot_name, n._dot_name)

    dot.render("test", format="png", cleanup=True)


x1 = AVar(5.0,1.0)

z = 3*(x1**sin(x1))

print(z.val, z.der)

draw_graph(z)

