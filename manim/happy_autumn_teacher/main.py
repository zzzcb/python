from manim import *

class Happy(Scene):
    def construct(self):
        text00 = Text(
            "祝",
            font_size=32,
            color="#B2C03D"
        ).move_to(6 * LEFT + 3 * UP)
        text0 = Text(
            "Bilibili的小伙伴",
            font_size=32,
            color="#B2C03D",
            weight=BOLD
        ).next_to(text00)
        text1 = Text(
            "中秋节",
            font_size=122,
            weight=BOLD,
            font="HGXC_CNKI",
            color="#B2C03D"
        ).shift(UP + 2.5 * LEFT)
        text11 = Text(
            "教师节",
            font_size=122,
            weight=BOLD,
            font="HGXC_CNKI",
            color="#B2C03D"
        ).next_to(text1, DOWN)
        text111 = Text(
            "快乐",
            font_size=122,
            weight=BOLD,
            font="HGXC_CNKI",
            color="#B2C03D"
        ).shift(2.5 * RIGHT)
        text2 = Text(
            "☺",
            font_size=144,
            weight=BOLD,
            color="#B2C03D"
        )
        text3 = Text(
            """
            ╭◜◝ ͡ ◜◝╮
            ( ˃̶͈◡˂̶͈ ) made base python manim
            ╰◟◞ ͜ ◟◞╯
            """,
            font_size=22,
            color="#B2C03D",
            font="JetBrainsMono-Regular"
        ).move_to(RIGHT * 4.5 + DOWN * 3)
        self.play(Write(text00), Write(text0))
        self.play(Write(text1), Write(text11), Write(text111))
        self.play(FadeOut(text1), FadeOut(text11), FadeOut(text111))
        self.remove(text00, text0)
        self.play(Write(text2.scale(5)), Write(text3))
        self.wait()