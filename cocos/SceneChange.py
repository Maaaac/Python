#coding:utf-8
import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.menu import *
from cocos.scenes.transitions import *
import pyglet
import NewScene

class GameLayer(Layer):
    is_event_handler=True
    def __init__(self):
        
        super(GameLayer,self).__init__()

        self.s_width,self.s_height=director.get_window_size()

        backgrund=Sprite('IMG.jpg')
        backgrund.position = self.s_width//2 , self.s_height//2
        self.add(backgrund,-1)

    def on_mouse_press(self,x,y,button,modifiers):
        print(x,y,button,modifiers)
        scene = NewScene.create_scene()
        #director.replace(scene)
        #director.push(scene)
        jzt=RotoZoomTransition(scene,1.5)
        director.push(jzt)

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu,self).__init__()
        #self.font_item["font_name"]=160
        #self.font_item_selected["font_size"]=160
        start_item=ImageMenuItem("1.png",self.on_start_item_callback)
        setting_item=ImageMenuItem("1.png",self.on_setting_item_callback)
        self.create_menu([start_item,setting_item],layout_strategy=fixedPositionMenuLayout([(530,400),(530,200)]))


    def on_start_item_callback(self):
        print("1")

    def on_setting_item_callback(self):
        print("2")



if __name__ == "__main__":
    director.init()
    main_scene=Scene(GameLayer())
    main_scene.add(MainMenu())
    director.run(main_scene)
