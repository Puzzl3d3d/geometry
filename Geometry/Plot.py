import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

fig, ax = plt.subplots()

polygons = []

def plot(shape, format="o"):
    print("\n\n\nPLOTTING SHAPE\n\n\n")
    array = []
    xpoints,ypoints = [], []

    for point in shape.points:
        array.append([point.x, point.y])
        xpoints.append(point.x)
        ypoints.append(point.y)

    print(array)

    print("\n\n\n\n")

    array = np.array(array)

    print(array)
    
    xpoints, ypoints = np.array(xpoints), np.array(ypoints)

    polygon = Polygon(array, closed=True)

    polygons.append(polygon)

    plt.plot(xpoints, ypoints, format)
def show(alpha=0.3):
    p = PatchCollection(polygons, alpha=alpha)

    colors = 1000*np.random.rand(len(polygons))
    p.set_array(np.array(colors))

    ax.add_collection(p)

    plt.show()