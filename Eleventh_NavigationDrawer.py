from kivymd.app import MDApp
from kivy.lang.builder import Builder

KV="""
<DrawerClickableItem@MDNavigationDrawerItem>
<DrawerLabelItem@MDNavigationDrawerItem>

MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title:"Umer"
                    elivation:4
                    md_bg_color:"black"
                    specific_text_color:"white"
                    pos_hint:{"top":1}
                    left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id:nav_drawer
            radius:(0, 16, 16, 0)

            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title:"Malik"
                    text:"mumermalik1245@gmail.com"
                    spacing:"40dp"
                    padding:"12dp",0,0,"32dp"
                MDNavigationDrawerLabel:
                    text:"Menu"
                DrawerClickableItem:
                    icon:"gmail"
                    right_text:"+99"
                    text:"Inbox"
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"
                MDNavigationDrawerLabel:
                    text:"Menu"
                DrawerClickableItem:
                    icon:"send"
                    text:"Message"
                DrawerClickableItem:
                    icon:"send"
                    text:"Inbox"
"""
class NavigationApp(MDApp):
    def build(self):
        bldr = Builder.load_string(KV)
        return bldr
NavigationApp().run()