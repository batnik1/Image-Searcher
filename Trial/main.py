from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Threebythreeone(BoxLayout):
    pass


class Noughtsandcrosses(BoxLayout):
    pass


class nandxApp(App):
    def build(self):
        return Noughtsandcrosses()


if __name__ == "__main__":
    nandxApp().run()