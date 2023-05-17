import matplotlib.pyplot as plt
import numpy as np

def plot(shape, format="o"):
    xpoints = []
    ypoints = []

    for point in shape.points:
        xpoints.append(point.x)
        ypoints.append(point.y)
    
    xpoints, ypoints = np.array(xpoints), np.array(ypoints)

    plt.plot(xpoints, ypoints, format)
def show():
    plt.show()