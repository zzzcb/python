from manim import *

########################
# 列举所有的可用字体
########################
def list_all_fonts():
    import manimpango
    print(manimpango.list_fonts())


########################
# text相关
########################
class TextDemo(Scene):
    def construct(self):
        plane = NumberPlane()  # new a grid plane
        self.add(plane)

        text = Text("你好 Python", font_size=32, font="JetBrain Mono", slant=ITALIC, weight=BOLD).shift(3 * UP)
        self.add(text)

        text2 = MarkupText(f'你好 <span color="{YELLOW}">Python</span>', color=RED).next_to(text, DOWN)
        self.add(text2)

        # t2c
        text3 = Text("你好 Python", font_size=32, font="JetBrain Mono", t2c={"[-6:-4]": BLUE}).next_to(text2, DOWN)
        self.add(text3)

        text4 = Text("你好 Python", font_size=32, font="JetBrain Mono", t2c={"Py": BLUE}).next_to(text3, DOWN)
        self.add(text4)

        text5 = Text("你好 Python", font_size=32, font="JetBrain Mono", t2c={"py": BLUE}).next_to(text4, DOWN)
        self.add(text5)

        # use gradient
        text6 = Text("你好 Python", font_size=32, font="JetBrain Mono", gradient=(RED, GREEN, BLUE)).next_to(text5,
                                                                                                             DOWN)
        self.add(text6)

        # use line_spacing  行距
        text7 = Text("你好\nPython", font_size=32, font="JetBrain Mono", line_spacing=1).next_to(text6, DOWN)
        self.add(text7)

        text8 = Text("你好\nPython", font_size=32, font="JetBrain Mono", line_spacing=3).next_to(text7)
        self.add(text8)

        # use disable_ligatures   禁用 连字
        li = Text("fl ligature", font_size=32).next_to(text7, DOWN)
        self.add(li)

        nli = Text("fl ligature", disable_ligatures=True, font_size=32).next_to(text8, DOWN)
        self.add(nli)

        # iter text 迭代遍历text对象
        google = Text("Google").move_to(UL * 3 + LEFT * 2)
        for c in google:
            c.set_color(random_bright_color())
        self.add(google)

        # Latex text
        tex = Tex("hello python").next_to(google, DOWN)
        self.add(tex)

        tex2 = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX').next_to(tex, DOWN)
        self.add(tex2)

        # math equation
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            font_size=20
        ).next_to(tex2, DOWN)
        self.add(equation)

        equation2 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            font_size=20,
            substrings_to_isolate='x'
        ).next_to(equation, DOWN)
        equation2.set_color_by_tex('x', YELLOW)
        self.add(equation2)

        # 对齐公式  &对齐   \\ 换行
        alignTex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6').next_to(equation2, DOWN)
        self.add(alignTex)


########################
# group相关
########################
class GroupDemo(Scene):
    def construct(self):
        square1 = Square()
        circle1 = Circle()
        square12 = Square()

        square2 = Square()
        circle2 = Circle()
        square22 = Square()

        g1 = Group(square1, circle1, square12).arrange().shift(2 * UP)
        g2 = Group(square2, circle2, square22).arrange(LEFT, buff=2).next_to(g1, DOWN)

        self.add(g1, g2)


if __name__ == '__main__':
    with tempconfig({"quality": "medium_quality", "preview": True}):
        d = TextDemo()
        d.render()
