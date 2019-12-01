from points import Point
from math import pi, sqrt

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        try:
            x = float(x)
            y = float(y)
            radius = float(radius)
        except ValueError:
            raise ValueError("Argumenty musza byc liczbami rzeczywistymi")
        else:
            if radius <= 0:
                raise ValueError("Promien ujemny lub rowny zero")
            else:
                self.pt = Point(x, y)
                self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise ValueError("Obiekt nie jest okregiem")

        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        return pi*self.radius**2

    def move(self, x, y):      # przesuniecie o (x, y)
        return Circle(self.pt.x+x, self.pt.y+y, self.radius)

    def cover(self, other):    # okrąg pokrywający oba

        s1s2 = sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)
        sub_r = abs(self.radius - other.radius)

        if s1s2 <= sub_r:
            if self.radius < other.radius:
                return other
            else:
                return self

        else:
            m = s1s2 + self.radius + other.radius
            p = self.pt + other.pt
            return Circle(p.x/2, p.y/2, m/2)