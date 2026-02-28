from manim import *

class TextTransform(Scene):
    def construct(self):
        text1 = Text('EfficientManim', font_size=48)
        text2 = Text('Beast Mode Activated', font_size=48).set_color(YELLOW)

        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1, text2))
        self.wait()
        