from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import requests as req


def main():
    n = 7
    r = Rectangle("синего", n, n)
    c = Circle("зеленого", n)
    s = Square("красного", n)
    print(r)
    print(c)
    print(s)

    r = req.get('https://api.github.com/events')
    print(r.status_code)


if __name__ == "__main__":
    main()