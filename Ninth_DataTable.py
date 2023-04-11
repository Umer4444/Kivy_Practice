from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.anchorlayout import MDAnchorLayout

class MyDataTableApp(MDApp):
    def build(self):
        layout = MDAnchorLayout()
        mytable =   MDDataTable(
           size_hint = (0.7,0.6),
           check = True,
           use_pagination = True,
           column_data = {
           ("No", dp(30)),
           ("Price",dp(30)),
           ("Name",dp(60))
           },
           row_data=[
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
           ("1","850","Pizza"),
          ] 

        )
        layout.add_widget(mytable)
        return layout
MyDataTableApp().run()