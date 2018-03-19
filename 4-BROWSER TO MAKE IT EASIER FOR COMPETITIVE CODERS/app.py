import toga
from toga.style.pack import *

prev=['https://google.com']
k=0

class Graze(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)

        self.webview = toga.WebView(style=Pack(flex=1))
        self.url_input = toga.TextInput(
            initial='https://github.com/anirudhkannanvp',
            style=Pack(flex=1, padding=5)
        )

        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button('GO', on_press=self.load_page, style=Pack(width=90, padding_right=10)),
                        toga.Button('HOME', on_press=self.load_page1, style=Pack(width=90, padding_right=10)),
                        toga.Button('BACK', on_press=self.load_page2, style=Pack(width=90, padding_right=10)),
                        toga.Button('TWITTER', on_press=self.load_page3, style=Pack(width=90, padding_right=10)),
                        toga.Button('YOUTUBE', on_press=self.load_page4, style=Pack(width=90, padding_right=10)),
                        toga.Button('LINKEDIN', on_press=self.load_page5, style=Pack(width=90, padding_right=10)),
                        toga.Button('HACKERRANK', on_press=self.load_page6, style=Pack(width=90, padding_right=10)),
                        toga.Button('CODECHEF', on_press=self.load_page7, style=Pack(width=90, padding_right=10)),
                        toga.Button('IDEONE', on_press=self.load_page8, style=Pack(width=90, padding_right=10))
                    ],
                    style=Pack(
                        direction=ROW
                    )
                ),
                self.webview,
            ],
            style=Pack(
                direction=COLUMN
            )
        )

        self.main_window.content = box
        t = self.url_input.value
        self.webview.url = str(t)
        prev.append(t)
        global k
        k+=1
        print(prev)

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        t = self.url_input.value
        self.webview.url = str(t)
        prev.append(t)
        global k
        k+=1
        print(prev)
    def load_page1(self, widget):
        self.webview.url = 'https://google.com'
    def load_page2(self, widget):
        global k
        self.webview.url = prev[k]
        k-=1
    def load_page3(self, widget):
        self.webview.url = 'https://twitter.com'
    def load_page4(self, widget):
        self.webview.url = 'https://youtube.com'
    def load_page5(self, widget):
        self.webview.url = 'https://in.linkedin.com/in/anirudh-kannan-v-p-951189140'
    def load_page6(self, widget):
        self.webview.url = 'https://www.hackerrank.com/anirudhkannan_v1'
    def load_page7(self, widget):
        self.webview.url = 'https://www.codechef.com/users/anirudhjarvis'
    def load_page8(self, widget):
        self.webview.url = 'https://ideone.com/'
def main():
    return Graze('Graze', 'org.pybee.graze')


if __name__ == '__main__':
    main().main_loop()
