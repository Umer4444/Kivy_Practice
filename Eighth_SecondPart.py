from kivymd.app import MDApp
from kivy.lang.builder import Builder

umer = """
MDScrollView:
    MDList:
        OneLineAvatarIconListItem:
            text: "Item1"
            IconLeftWidget:
                icon: "github"
            IconRightWidget:
                icon: "plus"

"""

class MyDialogBoxApp(MDApp):
    def build(self):
        bldr = Builder.load_string(umer)
        return bldr

MyDialogBoxApp().run()