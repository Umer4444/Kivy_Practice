from kivymd.app import MDApp
from kivymd.uix.label import *

class MyApp(MDApp):
    def build(self):
        icon = MDIcon(icon = "fingerprint")
        return icon

MyApp().run()