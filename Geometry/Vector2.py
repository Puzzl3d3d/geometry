import math

def isNumber(x): 
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)

class Vector2:
    def __init__(self, x, y):
        self.components = {"x": x, "y": y}
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __mul__(self, other):
        selfX, selfY = self.getComponents()

        if isNumber(other):
            return Vector2(selfX * other, selfY * other)
        
        otherX, otherY = other.getComponents()

        return Vector2(selfX * otherX, selfY * otherY)
    def __add__(self, other):
        selfX, selfY = self.getComponents()

        if isNumber(other):
            return Vector2(selfX + other, selfY + other)
        
        otherX, otherY = other.getComponents()

        return Vector2(selfX + otherX, selfY + otherY)
    def __div__(self, other):
        if isNumber(other):
            return self * (1 / other)
        return self * (other.inverse())
    def __sub__(self, other):
        return self + (-other)
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __ne__(self, __value):
        return not self == __value
    def __or__(self, __value):
        return self.x and self.y
    def __pow__(self, power):
        selfX, selfY = self.getComponents()

        if isNumber(power):
            return Vector2(selfX ** power, selfY ** power)
        
        otherX, otherY = power.getComponents()

        return Vector2(selfX ** otherX, selfY ** otherY)
    
    def magnitude(self):
        return abs(self.x) + abs(self.y)
    def inverse(self):
        selfX, selfY = self.getComponents()
        return Vector2(1/selfX, 1/selfY)
    def translate(self, other):
        return self + other
    def enlarge(self, sf, centre):
        enlarged = Vector2(self.x, self.y)

        enlarged -= centre
        enlarged *= sf
        enlarged += centre

        return enlarged
    def rotate(self, bearing, centre):
        radians = math.radians(-bearing)

        originX, originY = centre.getComponents()
        selfX, selfY = self.getComponents()

        rotatedX = originX + math.cos(radians) * (selfX - originX) - math.sin(radians) * (selfY - originY)
        rotatedY = originY + math.sin(radians) * (selfX - originX) + math.cos(radians) * (selfY - originY)

        return Vector2(rotatedX, rotatedY)
    def getComponents(self):
        return self.x, self.y