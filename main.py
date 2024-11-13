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
            return Square(data)
        elif shape_type == "Rectangle":
            return Rectangle(data)
        elif shape_type == "Circle":
            return Circle(data)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Perimeter {self.perimeter()} Area {self.area()}"


class Rectangle(Shape):
    def __init__(self, data: list) -> None:
        x1 = float(data[2])
        y1 = float(data[3])
        x2 = float(data[5])
        y2 = float(data[6])
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def perimeter(self) -> int | float:
        return 2 * (self.width + self.height)

    def area(self) -> int | float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, data: list) -> None:
        x1 = float(data[2])
        y1 = float(data[3])
        side = float(data[5])
        super().__init__(["Square", "TopRight",
                          x1, y1, "BottomRight",
                          x1+side,
                          y1+side])


class Circle(Shape):
    def __init__(self, data: list) -> None:
        self.radius = float(data[5])

    def perimeter(self) -> int | float:
        return round(2 * math.pi * self.radius, 2)

    def area(self) -> int | float:
        return round(math.pi * self.radius ** 2, 2)


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
