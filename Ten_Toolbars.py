from operator import imod
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from operator import imod

umer = """
MDBoxLayout:
    orientation:"vertical"
    MDTopAppBar:
        title:"Demo App"
        left_action_items:[["menu"]]
        right_action_items:[["clock"],["git"],["github"]]
        elevation:2
        
    MDBottomAppBar:
        MDTopAppBar:
            title:"Bottom"
            icon:"gitlab"
            type:"bottom"
            left_action_items:[["menu"]]
    
    MDLabel:
        text:"Hello"
        halign:"center"

"""

class MyDialogBoxApp(MDApp):
    def build(self):
        bldr = Builder.load_string(umer)
        return bldr

MyDialogBoxApp().run()