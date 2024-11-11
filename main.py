import math


class Shape:
    def perimeter(self) -> None:
        pass

    def area(self) -> None:
        pass

    @classmethod
    def create_shape(cls, data: list):
        shape_type = data[0]
        if shape_type == "Square":
            return Square(float(data[5]))
        elif shape_type == "Rectangle":
            return Rectangle(float(data[2]),
                             float(data[3]),
                             float(data[5]),
                             float(data[6]))
        elif shape_type == "Circle":
            return Circle(float(data[5]))
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


class Square(Shape):
    def __init__(self, side: int | float) -> None:
       self.side = side

    def perimeter(self) -> int | float:
        return 4 * self.side

    def area(self) -> int | float:
        return self.side ** 2

    def __str__(self) -> str:
        return f"Square Perimeter {self.perimeter()} Area {self.area()}"


class Rectangle(Shape):
    def __init__(self, x1: int | float,
                 y1: int | float,
                 x2: int | float,
                 y2: int | float) -> None:
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def perimeter(self) -> int | float:
        return 2 * (self.width + self.height)

    def area(self) -> int | float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle Perimeter {self.perimeter()} Area {self.area()}"


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def perimeter(self) -> int | float:
        return round(2 * math.pi * self.radius, 2)

    def area(self) -> int | float:
        return round(math.pi * self.radius ** 2, 2)

    def __str__(self) -> str:
        return f"Circle Perimeter {self.perimeter()} Area {self.area()}"


def main() -> None:
    shape_info = []
    with open("data_file.txt", 'r') as fh:
        for line in fh:
            if line.strip():
                print(line)
                data = line.split(" ")
                print(shape_info)
                shape = Shape.create_shape(data)
                print(shape)


if __name__ == '__main__':
    main()
