from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Red"  
        self.theme_cls.theme_style="Dark"                      
        btn4 = MDFillRoundFlatIconButton(text= "fingerprint", pos_hint={"center_x":0.5, "center_y":0.5})
        return btn4

MyApp().run()