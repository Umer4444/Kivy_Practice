from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFillRoundFlatIconButton

class MyApp(MDApp):
    def build(self):
        btn = MDFlatButton(text= "Click Me")
        btn2 = MDRectangleFlatButton(text= "fingerprint")
        btn3 = MDIconButton(icon= "fingerprint")
        btn4 = MDFillRoundFlatIconButton(icon= "fingerprint", pos_hint={"center_x":0.5, "center_y":0.5})
        return btn4

MyApp().run()