from ctypes import sizeof
from os import popen
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (1024,720)

import config
ms = ScreenManager()


Builder.load_string("""
<Login>
    benutzername: Benutzername.text
    pw: passwort.text
    knopf: btn
    GridLayout:
        cols:1
        size:root.width, root.height
        GridLayout:
            cols: 2
            Label: 
                text: "Benutzername"
                font_size: 30
            TextInput:
                id: Benutzername
                multiline: False
                font_size: 30
            Label:
                text: "Password"
                font_size: 30
            TextInput:
                id: passwort
                password: True
                multiline: False
                font_size: 30
        Button:
            text: "Anmelden"
            id: btn
            size_hint: (1.,0.5)
            font_size: 30
            on_release: 
                root.loginwithpopup()
                

<UserScreen>
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "User Bereich"
            font_size: 30
        Button:
            text: "zurück"
            font_size: 30
            on_release: 
                root.manager.current="Login"
                root.manager.transition.direction = "right"

""")

class Login(Screen):
    benutzername = StringProperty()
    pw = StringProperty
    knopf = ObjectProperty()

    def Anmelden(self):
        #print(self.benutzername)
        if self.benutzername == config.Benutzername and self.pw == config.Password:
            self.knopf.background_color=(0.,1.,0.,1.) # Green
            ms.current="Userscreen"
        else:
            self.knopf.background_color = (1.,0.,0.,1.)

    def loginwithpopup(self):
        if self.benutzername == "" or self.pw == "":
            popup = Popup(title = "Fehler", content = Label(text= "Passwort oder Benutzername leer !"), size_hint= (None,None), size = (400,400))
            popup.open()
        else:
            self.Anmelden()

class UserScreen(Screen):
    pass


ms.add_widget(Login(name="Login"))
ms.add_widget(UserScreen(name="Userscreen"))
class StartApp(App):
    def build(self):
        return(ms)



if __name__ == "__main__":
    StartApp().run()