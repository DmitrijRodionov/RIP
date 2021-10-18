from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure)
    FIGURE_TYPE = Прямоугольник

    @classmethod
    def get_figure_type(cls)
        return cls.FIGURE_TYPE

    def __init__(self, colorParam, widthParam, heightParam)
        self.width = widthParam
        self.height = heightParam
        self.figureColor = FigureColor()
        self.figureColor.colorproperty = colorParam

    def square(self)
        return self.width  self.height

    def __repr__(self)
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.figureColor.colorproperty,
            self.width,
            self.height,
            self.square()
        )