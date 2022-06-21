import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Window.size = (500, 700)

Builder.load_string('''
<CalcLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.height, root.width

        TextInput:
            id : calc_input
            text: "0"
            halign: "right"
            font_size: 40
            size_hint: (1, .15)

        GridLayout:pip
            cols: 4
            rows: 5

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "%"
                on_press : root.percent()


            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "CE"
                on_press: root.clear_entry()


            Button:
                id: clear
                size_hint: (.2, .2)
                font_size: 32
                text: "C"
                on_press: root.clear()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "/"
                on_press : root.math_sign("/")

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "7"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(7)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "8"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(8)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "9"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(9)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "X"
                on_press: root.math_sign("*")

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "4"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(4)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "5"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(5)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "6"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(6)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "-"
                on_press : root.math_sign("-")

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "1"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(1)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "2"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(2)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "3"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(3)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+"
                on_press: root.math_sign("+")

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "+/-"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press : root.pos_neg()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "0"
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.button_press(0)

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "."
                background_color: (157/255, 157/255, 157/155, 1)
                on_press: root.dot()

            Button:
                size_hint: (.2, .2)
                font_size: 32
                text: "="
                on_press : root.equal()

''')


class CalcLayout(BoxLayout):
    def clear(self):
        self.ids.calc_input.text = "0"

    def clear_entry(self):
        prior = self.ids.calc_input.text
        if prior == "0":
            pass
        elif len(prior) == 1:
            prior = "0"
        else:
            prior = prior[:-1]
        self.ids.calc_input.text = prior

    def percent(self):
        prior = self.ids.calc_input.text
        percentage = float(prior) * 0.01
        self.ids.calc_input.text = f"{percentage}"

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f'-{prior}'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def dot(self):
        prior = self.ids.calc_input.text

        num_list = prior.split("+")

        if ("+" or "*") in prior and "." not in num_list[:-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"

    def equal(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)

            self.ids.calc_input.text = str(answer)

        except:
            self.ids.calc_input.text = "Error"


class CalcApp(App):
    def build(self):
        return CalcLayout()


if __name__ == "__main__":
    CalcApp().run()

