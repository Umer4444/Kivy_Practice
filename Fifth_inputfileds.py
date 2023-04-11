from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton

class TextFieldApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        email = MDTextField(text="Enter your email", pos_hint={"center_x":0.5, "center_y":0.5})

        password = MDTextField(text="Password", pos_hint={"center_x":0.5, "center_y":0.5})

        button = MDFlatButton(text="Enter your email", pos_hint={"center_x":0.5, "center_y":0.5})

        layout.add_widget(email)
        layout.add_widget(password)
        layout.add_widget(button)
        return layout

TextFieldApp().run()