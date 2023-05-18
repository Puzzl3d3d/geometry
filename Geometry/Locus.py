from Geometry.Vector2 import Vector2
import random

class Locus:
    def __init__(self, *points):
        self.points = []

        for point in points:
            try:
                pointX, pointY = point
            except:
                pointX, pointY = point.x, point.y

            self.points.append(Vector2(pointX, pointY))

        print(self.points)
    def __eq__(self, other):
        return self.points == other.points
    def __mul__(self, other):
        points = []

        for vector2 in self.points:
            points.append(vector2 * other)

        self.points = points
    def __add__(self, other):
        points = []

        for vector2 in self.points:
            points.append(vector2 + other)

        self.points = points
    def __div__(self, other):
        points = []

        for vector2 in self.points:
            points.append(vector2 / other)

        self.points = points
    def __sub__(self, other):
        points = []

        for vector2 in self.points:
            points.append(vector2 - other)

        self.points = points
    def __neg__(self):
        points = []

        for vector2 in self.points:
            points.append(-vector2)

        self.points = points
    def __str__(self):
        output = ""

        for point in self.points:
            output += f"({point.x}, {point.y})\n"
        
        return output
    def __ne__(self, __value):
        return not self == __value
    def __or__(self, __value):
        return self.points and len(self.points) > 0
    def __pow__(self, power):
        points = []

        for vector2 in self.points:
            points.append(vector2 ** power)

        self.points = points
    
    def inverse(self):
       return 1/self
    def translate(self, other):
        return self + other
    def enlarge(self, sf, centre):
        points = []

        for vector2 in self.points:
            points.append(vector2.enlarge(sf, centre))

        self.points = points
    def rotate(self, bearing, centre):
        points = []

        for vector2 in self.points:
            points.append(vector2.rotate(bearing, centre))

        self.points = points
    def clone(self):
        points = []

        for point in self.points:
            points.append(point.clone())
        
        return Locus(*points)
    def randomPoint(self):
        return self.points[random.randint(1, len(self.points))]
    def randomPoints(self, n):
        return [self.randomPoint() for _ in range(n)]
    def centre(self):
        meanx, meany = 0, 0
        totalx, totaly = 0, 0

        for point in self.points:
            totalx += point.x
            totaly += point.y

        meanx, meany = totalx/len(self.points), totaly/len(self.points)

        return Vector2(meanx, meany)