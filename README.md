📜 Overview
This is a Python CLI application that reads 2D geometric shapes from standard input and calculates their perimeter and area. It currently supports the following shapes:

Square
Rectangle
Circle

The application is designed to be easily extensible, allowing new shapes to be added with minimal code changes.

🛠️ Features
Calculates perimeter and area for each shape.
Supports Square, Rectangle, Circle out of the box.
Designed with an extensible structure for adding more shapes in the future.
Provides detailed unit tests for each shape.
Handles input errors gracefully.

🏃‍♂️ How to Run
Clone the repository:
git clone <repository_url>
cd geometric-shapes-calculator

Run the application:
python main.py < data_file.txt

🔍 Input Format
The input consists of one or more lines, each specifying a 2D shape with its attributes. Here is the format for each supported shape:

Square:
Square TopRight <x> <y> Side <side_length>

Rectangle:
Rectangle TopRight <x1> <y1> BottomLeft <x2> <y2>

Circle:
Circle Center <x> <y> Radius <radius>

✅ Unit Tests
Unit tests are provided to ensure the correctness of the calculations. The tests cover all supported shapes.

To run the tests:

python -m unittest test_shapes.py
