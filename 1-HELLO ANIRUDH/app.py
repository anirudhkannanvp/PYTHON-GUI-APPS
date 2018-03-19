import toga


def button_handler(widget):
    print("Anirudh is great.Thanks for pressing the button")


def build(app):
    box = toga.Box()

    button = toga.Button('Is Anirudh Great or what?', on_press=button_handler)
    button.style.padding = 20
    button.style.set(margin=50);
    button.style.flex = 1
    box.add(button)

    return box


def main():
    return toga.App('First App', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    main().main_loop()
