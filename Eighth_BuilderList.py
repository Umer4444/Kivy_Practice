from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem

umer = """
MDScrollView:
    MDList:
        id:mylist
"""

class MyDialogBoxApp(MDApp):
    def build(self):
        bldr = Builder.load_string(umer)
        return bldr
    
    def on_start(self):
        for i in range(27):
            self.root.ids.mylist.add_widget(
                OneLineListItem(text=f"Item{i}")
            )

MyDialogBoxApp().run()