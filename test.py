import pytest
import math
from main import Square, Rectangle, Circle, Shape, create_shape

# Тести для класу Square
def test_square_perimeter():
    square = Square(["Square", "TopRight", "1", "1", "Side", '4'])
    assert square.perimeter() == 16

def test_square_area():
    square = Square(["Square", "TopRight", "1", "1", "Side", '4'])
    assert square.area() == 16

def test_square_str():
    square = Square(["Square", "TopRight", "1", "1", "Side", '3'])
    assert str(square) == "Square Perimeter 12.0 Area 9.0"

# Тести для класу Rectangle
def test_rectangle_perimeter():
    rectangle = Rectangle(["Rectangle", "TopRight", "0", "0", "BottomLeft", "3", "4"])
    assert rectangle.perimeter() == 14

def test_rectangle_area():
    rectangle = Rectangle(["Rectangle", "TopRight", "0", "0", "BottomLeft", "3", "4"])
    assert rectangle.area() == 12

def test_rectangle_str():
    rectangle = Rectangle(["Rectangle", "TopRight", "0", "0", "BottomLeft", "3", "4"])
    assert str(rectangle) == "Rectangle Perimeter 14.0 Area 12.0"

# Тести для класу Circle
def test_circle_perimeter():
    circle = Circle(["Circle", "Center", "1", "1", "Radius", "2"])
    assert circle.perimeter() == round(2 * math.pi * 2, 2)

def test_circle_area():
    circle = Circle(["Circle", "Center", "1", "1", "Radius", "2"])
    assert circle.area() == round(math.pi * 2 ** 2, 2)

def test_circle_str():
    circle = Circle(["Circle", "Center", "1", "1", "Radius", "1"])
    assert str(circle) == f"Circle Perimeter {round(2 * math.pi, 2)} Area {round(math.pi, 2)}"

# Тести для методу create_shape
def test_create_square():
    data = ["Square", "TopRight", "1", "1", "Side", "4"]
    shape = create_shape(data)
    assert isinstance(shape, Square)
    assert shape.perimeter() == 16
    assert shape.area() == 16

def test_create_rectangle():
    data = ["Rectangle", "TopRight", "4", "5", "BottomLeft", "1", "1"]
    shape = create_shape(data)
    assert isinstance(shape, Rectangle)
    assert shape.perimeter() == 14
    assert shape.area() == 12

def test_create_circle():
    data = ["Circle", "Center", "1", "1", "Radius", "2"]
    shape = create_shape(data)
    assert isinstance(shape, Circle)
    assert shape.perimeter() == round(2 * math.pi * 2, 2)
    assert shape.area() == round(math.pi * 2 ** 2, 2)

def test_create_shape_invalid():
    data = ["Triangle", "Point1", "0", "0", "Point2", "1", "1", "Point3", "2", "2"]
    with pytest.raises(ValueError):
        create_shape(data)