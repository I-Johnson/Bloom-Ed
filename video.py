from manimlib.imports import*
import numpy as np

class shapes(Scene):
    def construct(self):
        txt = TextMobject('Circle').scale(0.8).to_edge(UL)
        self.play(Write(txt))
        # self.wait(1)
        txt1 = TextMobject('Square').scale(0.8).to_edge(UR)
        self.play(Write(txt1))
        # self.wait(1)
        txt2 = TextMobject('Rectangle').scale(0.8).to_edge(DL)
        self.play(Write(txt2))
        # self.wait(1)
        txt3 = TextMobject('Triangle').scale(0.8).to_edge(DR)
        self.play(Write(txt3))
        # self.wait(1)
        txt4 = TextMobject('Ellipse').scale(0.8)
        self.play(Write(txt4))
        self.wait(1)

        shape1=Circle().scale(1)
        # shape1.set_fill()
        shape1.set_color(WHITE)
        shape1.to_edge(UL)
        self.play(Transform(txt, shape1, run_time=1))
        self.wait(1)

        fom1=TexMobject(r'A = {\pi}r^2').next_to(shape1, DOWN, buff=0.1).scale(0.8)
        self.play(Write(fom1), rate_func=rush_into)
        self.wait(1)

        shape2 = Square().scale(1)
        shape2.set_color(WHITE)
        shape2.to_edge(UR)
        self.play(Transform(txt1, shape2, run_time=1))
        self.wait(1)

        fom2=TexMobject(r'A = {l}^2').next_to(shape2, DOWN, buff=0.1).scale(0.8)
        self.play(Write(fom2), rate_func=rush_into)
        self.wait(1)

        shape3 = Rectangle().scale(0.8)
        shape3.set_color(WHITE)
        shape3.to_edge(DL, buff = 0.7)
        self.play(Transform(txt2, shape3, run_time=1))
        self.wait(1)

        fom3 = TexMobject(r'A = {l}*{b}').next_to(shape3, DOWN, buff=0.1).scale(0.8)
        self.play(Write(fom3), rate_func=rush_into)
        self.wait(1)

        shape4 = Triangle().scale(1)
        shape4.set_color(WHITE)
        shape4.to_corner(DR, buff=1)
        self.play(Transform(txt3, shape4, run_time=1))
        self.wait(1)

        fom4 = TexMobject(r'A = \frac{1}{2}bh').next_to(shape4, DOWN, buff=0.1).scale(0.8)
        self.play(Write(fom4), rate_func=rush_into)
        self.wait(1)

        shape5 = Ellipse().scale(1.5)
        shape5.set_color(WHITE)
        self.play(Transform(txt4, shape5), run_time=1)
        self.wait(1)

        fom5 = TexMobject(r'A = {\pi}*ab').next_to(shape5, DOWN, buff=0.1).scale(0.8)
        self.play(Write(fom5), rate_func=rush_into)
        self.wait(1)