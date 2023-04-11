from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

KV="""
ScreenManager:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name:"First"
    MDLabel:
        text:"Second Screen"
        halign:"center"
    MDRectangleFlatButton:
        text:"Second"
        pos_hint:{"center_x":0.5, "center_y":0.4}
        on_press:root.manager.current="Second"
<SecondScreen>:
    name:"Second"
    MDLabel:
        text:"First Screen"
        halign:"center"
    MDRectangleFlatButton:
        text:"First"
        pos_hint:{"center_x":0.5, "center_y":0.4}
        on_press:root.manager.current="First"
"""
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class MyApp(MDApp):
    def build(self):
        bldr = Builder.load_string(KV)
        return bldr
MyApp().run()