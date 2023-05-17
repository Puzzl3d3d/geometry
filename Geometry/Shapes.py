from Geometry.Locus import Locus as Shape
from Geometry.Vector2 import Vector2

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