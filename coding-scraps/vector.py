from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates, tolerance = 12 ):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            self.tolerance = tolerance
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format([ str(round(x,3)) for x in self.coordinates ] )


    def __eq__(self, rhs: "Vector"):
        return self.coordinates == rhs.coordinates

    def abs(self):
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))

    def normalized(self):
        try:
            abs = self.abs()
            if abs == 0:
                raise ZeroDivisionError
            return Vector([ x / abs  for x in self.coordinates ])
        except ZeroDivisionError:
            raise ZeroDivisionError("0-norm vector")

    def dot(self, rhs: "Vector"):
        try:
            if not self.dimension == rhs.dimension:
                raise ValueError
            return sum( [x * y for x,y in zip(self.coordinates,rhs.coordinates)] )
        except ValueError:
            raise ValueError("Dimensions are not matching")
        
    def angle(self,rhs: "Vector", in_degrees=False):
        v = self.normalized()
        w = rhs.normalized()
        vw = v.dot(w)
        radians = acos(round(vw, self.tolerance))
        if in_degrees:
            return degrees(radians)
        return radians
    
    def is_orthogonal(self, rhs: "Vector"):
        foo = self.dot(rhs)
        #print(foo)
        return round(foo, self.tolerance) == 0
    
    def is_parallel(self, rhs: "Vector"):
        if round(rhs.abs(),self.tolerance) == 0:
            return True
        angle = self.angle(rhs) 
        #print(angle)
        if round(angle,self.tolerance) == 0 or angle == round(pi,):
            return True
        return False
    
    def projection_onto(self, u: "Vector"):
        ub = u.normalized()                                 # create unit vector
        v_parallel = self.dot(ub)                           # get magnitude of v along u
        v_parallel = ub.scalar_multiplication(v_parallel)   # extend base with magnitude
        return v_parallel 

    def perpendicular_to(self, rhs: "Vector"):
        return self.subtract(self.projection_onto(rhs))     # v = v_p + v_t ==> v_t = v - v_p along u

    def add(self, rhs: "Vector"):
        return Vector([x + y for x,y in zip(self.coordinates, rhs.coordinates)])
    
    def subtract(self, rhs: "Vector"):
        return Vector([x - y for x,y in zip(self.coordinates, rhs.coordinates)])
    
    def scalar_multiplication(self, rhs):
        return Vector([x * rhs for x in self.coordinates])
    
    def scalar_divison(self, rhs):
        if rhs == 0:
            raise ZeroDivisionError
        return Vector([x / rhs for x in self.coordinates])
    
    def area_of_parallelogram(self, rhs: "Vector"):
        if self.dimension != rhs.dimension:
            raise ValueError("Dimensions do not match!")
        if self.dimension > 2:
            raise ValueError("Dimension too large")
        

    @staticmethod
    def to_rounded_string(s: str, p: int = 3):
        return "{0:.{1}f}".format(s,p)
            
# print("Coding magnitude and direction of vectors")
# v1 = Vector([-0.221,7.437])
# print("V1 magnitude: {}".format(Vector.to_rounded_string(v1.abs())))

# v2 = Vector([8.813, -1.331, -6.247])
# print("V2 magnitude: {}".format(Vector.to_rounded_string(v2.abs())))

# print("")

# v3 = Vector([5.581,-2.136])
# print("normalized vector v3: {}".format(v3.normalized()))

# v4 = Vector([1.996,3.108,-4.554])
# print("normalized vector v4: {}".format((v4.normalized())))

# print("")

# print("Coding dot product & angle")
# v5 = Vector([7.887, 4.138])
# w5 = Vector([-8.802,6.776])
# print("Dot product of v5, w5: {}".format(Vector.to_rounded_string(v5.dot(w5))))

# v6 = Vector([-5.955, -4.904, -1.874])
# w6 = Vector([-4.496, -8.755, 7.103])
# print("Dot product of v6, w6: {}".format(Vector.to_rounded_string(v6.dot(w6) ) ) )

# v7 = Vector([3.183,-7.627])
# w7 = Vector([-2.668, 5.319])
# print("Angle (rad) between v7, w7: {}".format(Vector.to_rounded_string(v7.angle(w7)))) 

# v8 = Vector([7.35, 0.221, 5.188])
# w8 = Vector([2.751, 8.259, 3.985])
# print("Angle (degrees) between v8, w8: {}".format(Vector.to_rounded_string(v8.angle(w8, in_degrees=True))))

# print("")

# print("Checking for parallelism & orthogonality")
# print("9")
# v9 = Vector([-7.579,-7.88])
# w9 = Vector([22.737, 23.64])
# if (v9.is_parallel(w9)):
#     print("v9, w9, are parallel")
# if (v9.is_orthogonal(w9)):
#     print("v9, w9, are orthogonal")
# print("")
# print("10")
# v10 = Vector([-2.029, 9.97, 4.172])
# w10 = Vector([-9.231, -6.639, 7.245])
# if (v10.is_parallel(w10)):
#     print("v10, w10, are parallel")
# if (v10.is_orthogonal(w10)):
#     print("v10, w10, are orthogonal")
# print("")
# print("11")
# v11 = Vector([-2.328, -7.284, -1.214])
# w11 = Vector([-1.821, 1.072, -2.94])
# if (v11.is_parallel(w11)):
#     print("v11, w11, are parallel")
# if (v11.is_orthogonal(w11)):
#     print("v11, w11, are orthogonal")
# print("")
# print("self.tolerance")
# v12 = Vector([2.118, 4.827])
# w12 = Vector([0,0])
# if (v12.is_parallel(w12)):
#     print("v12, w12, are parallel")
# if (v12.is_orthogonal(w12)):
#     print("v12, w12, are orthogonal")
# print("")

print("")
print("Coding vector projections")
v13 = Vector([3.039, 1.879])
b13 = Vector([0.825, 2.036])
v13p = v13.projection_onto(b13)
v13t = v13.perpendicular_to(b13)
print("Projection: {}".format(v13p))
v14 = Vector([-9.88, -3.264, -8.159])
b14 = Vector([-2.155, -9.353, -9.473])
v14p = v14.projection_onto(b14)
v14t = v14.perpendicular_to(b14)
print("Normal: {}".format(v14t))
v15 = Vector([3.009, -6.172, 3.692, -2.51])
b15 = Vector([6.404, -9.144, 2.759, 8.718])
v15p = v15.projection_onto(b15)
v15t = v15.perpendicular_to(b15)
print("Added: {} + {}".format(v15p,v15t))
print("")