from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Menu(Screen):
    ...

class Game(Screen):
    ...

class VictApp(App):
    def build(self):
        self.manager = ScreenManager()

        self.manager.add_widget(Menu(name='menu'))
        self.manager.add_widget(Game(name='game'))

        return self.manager

app = VictApp()

app.run()
