from Geometry.Locus import Locus as Shape
from Geometry.Vector2 import Vector2

import math

# From top left
def Square(tl, sidelength):
    return Shape(
        [tl.x, tl.y],
        [tl.x + sidelength, tl.y],
        [tl.x, tl.y + sidelength],
        [tl.x + sidelength, tl.y + sidelength]
    )
def EqualTriange(tl, sidelength):
    return Shape(
        [tl.x + (sidelength/2), tl.y],
        [tl.x, tl.y - sidelength],
        [tl.x + sidelength, tl.y - sidelength]
    )
def Circle(tl, size, iters):
    points = []
    for angle in range(0, 360, round(360/iters)):
        x = math.sin(math.radians(angle)) * size
        y = math.cos(math.radians(angle)) * size

        points.append(Vector2(x + tl.x, y + tl.y))
    return Shape(*points)