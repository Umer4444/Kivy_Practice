from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class MyDialogBoxApp(MDApp):
    def build(self):
        close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        more_btn = MDFlatButton(text="More")

        self.dialog = MDDialog(title="Name", text="Muhammad Umer Malik", size_hint=(0.7,1), buttons=[close_btn,more_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dissmiss()

MyDialogBoxApp().run()