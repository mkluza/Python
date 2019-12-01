from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        try:
            x1 = float(x1)
            y1 = float(y1)
            x2 = float(x2)
            y2 = float(y2)
            x3 = float(x3)
            y3 = float(y3)
        except ValueError:
            raise ValueError("Wierzcholki musza byc liczbami rzeczywistymi")
        else:
            self.pole = 1/2 * abs((x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1))
            if self.pole == 0:
                raise ValueError("Wierzcholki nie moga byc wspolliniowe")
            else:
                self.pt1 = Point(x1, y1)
                self.pt2 = Point(x2, y2)
                self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({0}, {1}), ({2}, {3}), ({4}, {5})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({0}, {1}, {2}, {3}, {4}, {5})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)


    def __eq__(self, other):    # obsługa tr1 == tr2
        if not isinstance(other, Triangle):
            raise ValueError("Obiekt nie jest trojkatem")

        x = sorted([self.pt1.x, self.pt2.x, self.pt3.x])
        y = sorted([self.pt1.y, self.pt2.y, self.pt3.y])
        o_x = sorted([other.pt1.x, other.pt2.x, other.pt3.x])
        o_y = sorted([other.pt1.y, other.pt2.y, other.pt3.y])
        return (x == o_x) and (y == o_y)

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek trójkąta
        center = self.pt1 + self.pt2 + self.pt3
        x = center.x/3
        y = center.y/3
        return Point(x, y)


    def area(self):             # pole powierzchni
        return self.pole

    def move(self, x, y):      # przesunięcie o (x, y)
        return Triangle(self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y, self.pt3.x+x, self.pt3.y+y)


    def make4(self):           # zwraca listę czterech mniejszych
        p = Point(abs(self.pt1.x - self.pt2.x), abs(self.pt1.y - self.pt2.y))
        p1 = Point(p.x/2, p.y/2)
        p2 = Point(p.x/3, p.y/3)
        p3 = Point(p.x/4, p.y/4)
        p4 = Point(p.x/6, p.y/6)

        smaller = list()
        smaller.append(Triangle(self.pt1.x, self.pt1.y, self.pt1.x+p1.x, self.pt1.y+p1.y, self.pt3.x, self.pt3.y))
        smaller.append(Triangle(self.pt1.x, self.pt1.y, self.pt1.x+p2.x, self.pt1.y+p2.y, self.pt3.x, self.pt3.y))
        smaller.append(Triangle(self.pt1.x, self.pt1.y, self.pt1.x+p3.x, self.pt1.y+p3.y, self.pt3.x, self.pt3.y))
        smaller.append(Triangle(self.pt1.x, self.pt1.y, self.pt1.x+p4.x, self.pt1.y+p4.y, self.pt3.x, self.pt3.y))
        return smaller

