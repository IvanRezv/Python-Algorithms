from math import pi

class Square(object):
    def area(self,side):
        return side * side
    def perimetr(self,side):
        return 4 * side

class Rectangle(object):
    def area(self,side,height):
        return  (0.5*(side * height))
    def perimetr(self,side_a,side_b,side_c):
        return side_a + side_b + side_c

class Romb(object):
    def area(self, side, height):
        return side * height
    def perimetr(self,side):
        return 4 * side
 
class Pryamougolnik(object):
    def area(self, side_a, side_b):
        return side_a * side_b
    def perimetr(self, side_a, side_b):
        return (side_a * 2) + (side_b * 2)
 
class Ellipse(object):
    def perimetr(self, pol_a, pol_b):
        pi = float(3.14)
        return 4 * (pi*pol_a*pol_b + pow((pol_a - pol_b),2))/(pol_b+pol_a)
    def area(self, pol_a, pol_b):
        pi = float(3.14)
        return pi * pol_a * pol_b