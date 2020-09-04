#coding:utf-8
import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.menu import *
from cocos.scenes.transitions import *
from cocos.actions import *
import Guess_game
import Guess_rule

class Guess_menu(Layer):
    is_event_handler=True
    def __init__(self):
        super(Guess_menu,self).__init__()
        self.s_width,self.s_height=director.get_window_size()
        background = Sprite("IMG/图片1.png")
        background.position = self.s_width/2,self.s_height/2
        self.add(background)

        background1 = Sprite("IMG/27.png")
        background1.position = 400,200
        self.add(background1)

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.font_item['font_size']=80
        self.font_item_selected['font_size']=120

        start_item=ImageMenuItem('IMG/23_1.png',self.on_start_item_callback)
        setting_item=ImageMenuItem('IMG/23_2.png',self.on_setting_item_callback)
        rule_item=ImageMenuItem('IMG/23_5.png',self.on_rule_item_callback)
        exit_item=ImageMenuItem('IMG/23_4.png',self.on_exit_item_callback)

        self.create_menu([start_item,setting_item,rule_item,exit_item],layout_strategy=fixedPositionMenuLayout([(100,380),(300,380),(500,380),(700,380)]))

    def on_start_item_callback(self):
        print("on_start_item_callback")
        scene = Guess_game.create_scene()
        director.replace(scene)

    def on_setting_item_callback(self):
        print("on_setting_item_callback")

    def on_rule_item_callback(self):
        print("on_return_item_callback")
        scene = Guess_rule.create_scene()
        director.replace(scene)

    def on_exit_item_callback(self):
        print("on_exit_item_callback")
        exit()

'''
if __name__ == "__main__":
    director.init(width=800,height=450,caption='Guess Game 游戏菜单')
    main_scene=Scene(Guess_menu())
    main_scene.add(MainMenu())
    director.run(main_scene)
'''

def Acreate_scene():
    main_scene=Scene(Guess_menu())
    main_scene.add(MainMenu())
    return main_scene