from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import Screen
style = """
MDBoxLayout:
    orientation:"vertical"
    padding:90
    spacing:10

    MDTextField:
        hint_text:"Enter your name"
        helper_text:"Username must be unique"
        helper_text_mode:"on_focus"
        icon_left:"account"
        pos_hint:{"center_x":0.5, "center_y":0.5}
        size_hint_x:None
        width:300

    MDTextField:
        hint_text: "Enter your password"
        helper_text: ""
        helper_text_mode: "on_focus"
        icon_left: "lock-off"
        pos_hint:{"center_x":0.5, "center_y":0.5}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text:"Login"
        pos_hint:{"center_x":0.5, "center_y":0.5}
"""
class TextField(MDApp):
    def build(self):
        scrn = Screen()
        bldr = Builder.load_string(style)
        scrn.add_widget(bldr)
        return scrn
TextField().run()