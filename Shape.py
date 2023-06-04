# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File : Shape.py
# Description : 
# Author : yc0325lee
# Created : 2021-06-20 20:08:38 by lee2103
# Modified : 2021-06-20 20:08:38 by lee2103
#
#    Shape__Common => {
#        Shape__Base => {
#            Shape__OneDimensional => {
#                Shape__Dot => {},
#                Shape__Line => {},
#            },
#            Shape__TwoDimensional => {
#                Shape__Circle => {},
#                Shape__Square => {},
#                Shape__Triangle => {},
#            },
#            Shape__ThreeDimensional => {
#                Shape__Sphere => {},
#                Shape__Cube => {},
#                Shape__Tetrahedron => {},
#            },
#        },
#
# ----------------------------------------------------------------------------

# -------------------------------------
# Shape__Base
class Shape__Base:
    activeCount = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Shape__Base.activeCount += 1

    @classmethod
    def count(cls):
        return cls.activeCount

    def dump(self):
        #print("self=", self, end=' ')
        print("type(self)=", type(self), end=' ')
        print("name=", self.name, end=' ')
        print("color=", self.color, end=' ')
    pass

# -------------------------------------
# Shape__OneDimensional
class Shape__OneDimensional(Shape__Base):
    activeCount = 0
    def __init__(self, name, color):
        super().__init__(name, color)
        __class__.activeCount += 1
    pass

class Shape__Dot(Shape__OneDimensional):
    activeCount = 0
    def __init__(self, name, color, thickness):
        super().__init__(name, color)
        self.thickness = thickness
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("thickness=", self.thickness)
    pass

class Shape__Line(Shape__OneDimensional):
    activeCount = 0
    def __init__(self, name, color, length):
        super().__init__(name, color)
        self.length = length
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("length=", self.length)
    pass


# -------------------------------------
# Shape__TwoDimensional
class Shape__TwoDimensional(Shape__Base):
    activeCount = 0
    def __init__(self, name, color):
        super().__init__(name, color)
        __class__.activeCount += 1
    pass

class Shape__Circle(Shape__TwoDimensional):
    activeCount = 0
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("radius=", self.radius)
    pass

class Shape__Square(Shape__TwoDimensional):
    activeCount = 0
    def __init__(self, name, color, sideLength):
        super().__init__(name, color)
        self.sideLength = sideLength
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("sideLength=", self.sideLength)
    pass

class Shape__Triangle(Shape__TwoDimensional):
    activeCount = 0
    def __init__(self, name, color, baseLength, height):
        super().__init__(name, color)
        self.baseLength = baseLength
        self.height = height
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("baseLength=", self.baseLength, end=' ')
        print("height=", self.height)
    pass


# -------------------------------------
# Shape__ThreeDimensional
class Shape__ThreeDimensional(Shape__Base):
    activeCount = 0
    def __init__(self, name, color):
        super().__init__(name, color)
        __class__.activeCount += 1
    pass

class Shape__Sphere(Shape__ThreeDimensional):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("radius=", self.radius)
    pass

class Shape__Cube(Shape__ThreeDimensional):
    def __init__(self, name, color, edgeLength):
        super().__init__(name, color)
        self.edgeLength = edgeLength
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("edgeLength=", self.edgeLength)
    pass

class Shape__Tetrahedron(Shape__ThreeDimensional):
    def __init__(self, name, color, edgeLength):
        super().__init__(name, color)
        self.edgeLength = edgeLength
        __class__.activeCount += 1

    def dump(self):
        super().dump()
        print("edgeLength=", self.edgeLength)
    pass





# -------------------------------------
# main.py
if __name__ == "__main__":
    import sys

    modules = [
        Shape__Base,
        Shape__OneDimensional,
        Shape__Dot,
        Shape__Line,
        Shape__TwoDimensional,
        Shape__Circle,
        Shape__Square,
        Shape__Triangle,
        Shape__ThreeDimensional,
        Shape__Sphere,
        Shape__Cube,
        Shape__Tetrahedron
    ]

    print("# " + "-" * 37, "\n# count - before")
    for module in modules:
        print("{}.count()= {}".format(module.__name__, module.count()))
    print()
    
    shapes = [
        Shape__Dot         ( "dot",         "black", 1 ),
        Shape__Line        ( "line",        "black", 2 ),
        Shape__Circle      ( "circle",      "black", 3 ),
        Shape__Square      ( "square",      "black", 4 ),
        Shape__Triangle    ( "triangle",    "black", 5, 9 ),
        Shape__Sphere      ( "sphere",      "black", 6 ),
        Shape__Cube        ( "cube",        "black", 7 ),
        Shape__Tetrahedron ( "tetrahedron", "black", 8 ),
    ]
    
    # polymorphism
    for shape in shapes:
        shape.dump()
    
    print()
    
    print("# " + "-" * 37, "\n# count - after")
    for module in modules:
        print("{}.count()= {}".format(module.__name__, module.count()))
    print()
    
    for shape in shapes:
        if isinstance(shape, Shape__Triangle):
            print("[info] Triangle instance found")
            shape.dump()
        elif isinstance(shape, Shape__Tetrahedron):
            print("[info] Tetrahedron instance found")
            shape.dump()
        else:
            pass

    
    print("# attributes of", shapes[0])
    for attr in dir(shapes[0]):
        if '__' not in attr:
            print("attr=", attr)

    print("shapes[0].__class__", shapes[0].__class__)

    #print("get_count=", shapes[0].get_count())
