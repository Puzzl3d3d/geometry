from Geometry.Locus import Locus as Shape
from Geometry.Vector2 import Vector2
from Geometry.Plot import plot, show
import Geometry.Shapes as Shapes

square = Shape(
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
)

print(square)

plot(square)

square.enlarge(5, Vector2(0.5,0.5))

print(square)

plot(square, format="x")

square.rotate(20, Vector2(0, 0))

print(square)

plot(square, format=">")

# Shape

triangle = Shapes.EqualTriange(Vector2(0,0), 5)

plot(triangle, format="<")

circle = Shapes.Circle(Vector2(0,0), 3, 50)

plot(circle, "o")

show()
