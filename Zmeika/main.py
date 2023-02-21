from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Menu(Screen):
    ...

class Game(Screen):
    ...

class Pos(Widget):
    # def __init__(self, x,y, size):
    #     super().__init__()
    #     self.size = (size, size)
    #     self.pos = (x,y)
    ...

# class Game1(Widget):
#     def __init__(self):
#         super().__init__(self)
#         self.poss = Pos(120,120, 40)
#         self.add_widget(self.poss)

class ZmeikaApp(App):
    def build(self):
        self.manager = ScreenManager()

        self.manager.add_widget(Menu(name='menu'))
        self.manager.add_widget(Game(name='game'))

        return self.manager

if __name__ == '__main__':
    ZmeikaApp().run()
