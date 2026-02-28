from manim import *

class VGroupExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(5)])
        dots.arrange(RIGHT, buff=0.8)

        self.play(FadeIn(dots))
        self.play(dots.animate.shift(UP))
        self.wait()
        