from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.scrollview import MDScrollView

class MyDialogBoxApp(MDApp):
    def build(self):
        my_scroll = MDScrollView()
        my_list = MDList()
        item_1 = OneLineListItem(text="Umer")
        item_2 = TwoLineListItem(text="Umer", secondary_text="Welcome")
        item_3 = ThreeLineListItem(text="Umer", secondary_text="Yes", tertiary_text="No")

        my_scroll.add_widget(my_list)
        my_list.add_widget(item_1, item_2, item_3)

        return my_scroll
MyDialogBoxApp().run()