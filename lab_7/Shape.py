import numpy as np

class Shape(object):
    """docstring for Shape."""
    def __init__(self,movable):
        self.movable = movable

    def create_shape():
        pass

class Circle(Shape):
    """docstring for Circle."""

    def __init__(self, center, radius, sectors, movable = False):
        super(Circle, self).__init__(movable)
        self.center = center
        self.radius = radius
        self.sectors = sectors
        self.movable = movable

    def create_shape(self):
        res = [[0., 0., 0.]]
        for i in range(self.sectors):
            x = self.center[0] + self.radius * np.cos(i * 2*np.pi/self.sectors)
            y = self.center[0] + 0
            z = self.center[1] + self.radius * np.sin(i * 2*np.pi/self.sectors)
            res.append([x,y,z])
            res.append([0., 0., 0.])
            res.append(res[len(res)-2])

        res.append(res[1])
        res.append(res[len(res)-3])

        return np.array(res)

class Cylindre(Shape):
    """docstring for Cylindre."""
    def __init__(self, center, radius, height, sectors, movable = False):
        super(Cylindre, self).__init__(movable)
        self.center = center
        self.radius = radius
        self.height = height
        self.sectors = sectors
        self.movable = movable

    def create_shape(self):
        center_1 = [self.center[0], self.center[1] + self.height/2, self.center[2]]
        circle_up = Circle(center_1, self.radius, self.sectors, self.movable).create_shape()
        circle_down = circle_up - np.array([0, self.height , 0])
        res = circle_up.tolist()
        res += circle_down.tolist()

        verticals = []
        for i in range(3, circle_up.shape[0], 3):
            verticals.append(circle_up[i+1].tolist())
            verticals.append(circle_up[i].tolist())
            verticals.append(circle_down[i+1].tolist())
            #
            verticals.append(circle_up[i])
            verticals.append(circle_down[i])
            verticals.append(circle_down[i+1])

        res += verticals
        return np.array(res)

class Sphere(Shape):
    """docstring for Sphere."""
    def __init__(self, center, radius, sectors, stacks, movable = False):
        super(Sphere, self).__init__(movable)
        self.center = center
        self.radius = radius
        self.sectors = sectors
        self.stacks = stacks
        self.movable = movable

    def generate_points(self):
        res = [[self.center[0], self.center[1]  + self.radius, self.center[2]]]
        for i in range(self.stacks):
            phi = np.pi/2  - i * np.pi/self.stacks
            for j in range(self.sectors):
                theta = j * 2*np.pi/self.sectors  # must be 2 * pi
                # print(int(theta*100)/100)
                x = self.center[0] + self.radius * np.sin(phi) * np.sin(theta)
                y = self.center[1] + self.radius * np.cos(phi)
                z = self.center[2] + self.radius * np.sin(phi) * np.cos(theta)
                res += [[x, y, z]]
        return np.array(res)

    def create_shape(self):
        arr = self.generate_points()
        print(arr)
        res = []
        up_part = []
        down_part = []
        inv = np.array([1, -1, 1])

        for i in range(1,self.sectors):
            up_part += [arr[0].tolist(), arr[i].tolist(), arr[i+1].tolist()]
            down_part += [(arr[0]*inv).tolist(),(arr[i]*inv).tolist(), (arr[i+1]*inv).tolist()]
            if i == self.sectors-1 :
                up_part += [arr[0].tolist(), arr[1].tolist(), arr[-1].tolist()]
                down_part += [(arr[0]*inv).tolist(),(arr[1]*inv).tolist(), (arr[-1]*inv).tolist()]


        major_part = [[]]
        for i in range(self.sectors, self.sectors*(self.stacks-2)):
            pass

        # print('up_part\n',np.array(up_part))
        # print('down_part\n',np.array(down_part))
        res += up_part
        res += down_part
        return np.array(res)
