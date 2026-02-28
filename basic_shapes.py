from manim import *

class BasicShapes(Scene):
    def construct(self):
        circle = Circle(color=BLUE).shift(LEFT)
        square = Square(color=GREEN).shift(RIGHT)
        triangle = Triangle(color=RED).shift(UP)

        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.wait()
        