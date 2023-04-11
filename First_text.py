from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class HelloApp(MDApp): 
    def build(self):
        txt = MDLabel(text="Umer", halign = "center", font_style= "H2", theme_text_color= "Secondary")
        return txt
    
HelloApp().run()