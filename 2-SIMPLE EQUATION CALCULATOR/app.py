import toga
from toga.style.pack import *


def build(app):
    a_box = toga.Box()
    b_box = toga.Box()
    c_box = toga.Box()
    d_box = toga.Box()
    box = toga.Box()

    a_input = toga.TextInput()
    b_input = toga.TextInput()
    c_input = toga.TextInput()
    d_input = toga.TextInput()

    a_label = toga.Label('OPERAND-2', style=Pack(text_align=LEFT))
    b_label = toga.Label('OPERAND-1', style=Pack(text_align=LEFT))
    c_label = toga.Label('OPERATOR', style=Pack(text_align=LEFT))
    d_label = toga.Label('EQUATION ANSWER', style=Pack(text_align=LEFT))
    

    def calculate(widget):
        try:
        	temp_a=str(a_input.value)
        	temp_b=str(b_input.value)
        	temp_c=str(c_input.value)
        	temp_d=str(temp_a+temp_c+temp_b)
        	d_input.value = eval(temp_d)
        except:
            d_input.value = '???'

    button = toga.Button('Calculate The equation', on_press=calculate)

    b_box.add(b_input)
    b_box.add(b_label)

    a_box.add(a_input)
    a_box.add(a_label)

    c_box.add(c_input)
    c_box.add(c_label)

    d_box.add(d_input)
    d_box.add(d_label)

    box.add(b_box)
    box.add(a_box)
    box.add(c_box)
    box.add(d_box)
    box.add(button)

    box.style.update(direction=COLUMN, padding_top=10)
    b_box.style.update(direction=ROW, padding=5)
    a_box.style.update(direction=ROW, padding=5)
    c_box.style.update(direction=ROW, padding=5)
    d_box.style.update(direction=ROW, padding=5)

    a_input.style.update(flex=1)
    b_input.style.update(flex=1)
    c_input.style.update(flex=1)
    d_input.style.update(flex=1)
    a_label.style.update(width=100, padding_left=10)
    b_label.style.update(width=100, padding_left=10)
    c_label.style.update(width=100, padding_left=10)
    d_label.style.update(width=100, padding_left=10)

    button.style.update(padding=15, flex=1)

    return box


def main():
    return toga.App('ANIRUDH S Simple equation Evaluator', 'org.pybee.b_to_c', startup=build)


if __name__ == '__main__':
    main().main_loop()
