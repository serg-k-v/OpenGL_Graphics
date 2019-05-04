import numpy as np

class Shape(object):
    """docstring for Shape."""
    def __init__(self):
        pass

    def create_shape():
        pass


class Circle(Shape):
    """docstring for Circle."""

    def __init__(self, center, radius, n_sides):
        self.center = center
        self.radius = radius
        self.n_sides = n_sides

    def create_shape(self):
        x = []
        y = []
        z = []
        for i in range(self.n_sides + 2):
            y.append(0)
            x.append( self.center[0] + self.radius * np.cos(i * 2*np.pi/self.n_sides) )
            z.append( self.center[1] + self.radius * np.sin(i * 2*np.pi/self.n_sides) )

        return np.array([x, y, z]).transpose()

class Cylindre(Shape):
    """docstring for Cylindre."""
    def __init__(self, center, radius, height, n_sides):
        super(Cylindre, self).__init__()
        self.center = center
        self.radius = radius
        self.n_sides = n_sides
        self.height = height

    def create_shape():
        pass

class Sphere(Shape):
    """docstring for Sphere."""
    def __init__(self, arg):
        super(Sphere, self).__init__()
        self.arg = arg
