import math

class Vector:
    def __init__(self, *args):
        self.dimention = list(args)

    def __str__(self):
        return f"Vector{tuple(self.dimention)}"
    
    def __len__(self):
        return len(self.dimention)
    
    def check_dimension(self, other):
        if len(self) != len(other):
            return ValueError("Vectors must have the same dimention")
    
    def __add__(self, other):
        self.check_dimension(other)
        new_dimention = [a + b for a, b in zip(self.dimention, other.dimention)]
        return Vector(*new_dimention)
    
    
    def __sub__(self, other):
        self.check_dimension(other)
        new_dimention = [a-b for a, b in zip(self.dimention, other.dimention)]
        return Vector(*new_dimention)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            self.check_dimension(other)
            return sum(a*b for a, b, in zip(self.dimention, other.dimention))
        elif isinstance(other, (int, float)):
            new_dimention = [a*other for a in self.dimention]
            return Vector(*new_dimention)
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.dimention))
    
    def normalize(self):
        mag = self.magnitude()
        if not(mag):
            return ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.dimention])
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1) 

# Addition   
v3 = v1 + v2
print(v3) 

# Subtraction
v4 = v2 - v1
print(v4)

# Dot product
dot_product = v1 * v2
print(dot_product)

# Scalar multiplication
v5 = 3 * v1
print(v5) 

# Magnitude
print(v1.magnitude())

# Normalization
v_unit = v1.normalize()
print(v_unit)