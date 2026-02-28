from manim import *

class ValueTrackerExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)

        number = always_redraw(
            lambda: DecimalNumber(
                tracker.get_value(),
                num_decimal_places=2
            ).to_edge(UP)
        )

        square = Square().scale(0.5)

        self.add(number, square)
        self.play(tracker.animate.set_value(10), square.animate.rotate(PI))
        self.wait()
        