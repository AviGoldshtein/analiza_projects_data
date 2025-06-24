from shapes.Circle import Circle
from shapes.Square import Square
from shapes.Hexagon import Hexagon
from shapes.Triangle import Triangle
from shapes.Rectangle import Rectangle

if __name__ == "__main__":
    all_shapes = []

    a = Circle(5)
    b = Hexagon(10)
    c = Square(4)
    d = Triangle(4, 3, 5)
    e = Rectangle(10, 4)

    all_shapes.append(a)
    all_shapes.append(b)
    all_shapes.append(c)
    all_shapes.append(d)
    all_shapes.append(e)

    for shape in all_shapes:
        print(shape)
        print(f" area: {shape.get_area()}")
        print(f" scope: {shape.get_scope()}")