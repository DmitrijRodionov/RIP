from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, colorParam, rParam):
        self.r = rParam
        self.figureColor = FigureColor()
        self.figureColor.colorproperty = colorParam

    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.figureColor.colorproperty,
            self.r,
            self.square()
        )