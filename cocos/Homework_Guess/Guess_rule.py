#coding:utf-8
import cocos
import pyglet
import random
from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.menu import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.sprite import Sprite
from cocos.text import *
import Guess_game
import Guess_menu


class Guess_rule(Layer):
    is_event_handler=True
    def __init__(self):
        super(Guess_rule,self).__init__()
        self.s_width,self.s_height=director.get_window_size()
        background = Sprite("IMG/图片1.png")
        background.position = self.s_width/2,self.s_height/2
        self.add(background,-1)

        background1 = Sprite("IMG/18.png")
        background1.position = 50,50
        self.add(background1,1)

        lable = Label('Game Rlue',
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center',anchor_y = 'top',color=(7,7,14,200))
        lable.position = 400,450
        self.add(lable,1)

        rule= u'''系统会随机生成一个没有重复数字的4位数序列 
        输入你猜想的序列，每猜一次 
        系统会根据你输入的的序列给出XAXB 
        其中A前面的数字表示位置正确的数的个数 
        而B前面的数字表示数字正确而位置不对的数的个数。
        '''

        text = Label(rule,
            font_name = 'Times New Roman',
            font_size = 15,
            anchor_x = 'center',anchor_y = 'top',color=(7,7,14,200),width = 20,multiline = True)
        text.position=100,400
        self.add(text,1)

        setcomm = u'''游戏有如下特殊指令：
        查看答案：SELECTANSWER------重置序列：RE
        修改序列：MODIFIEDTOXXXX
        PS：游戏仅支持英文输入法，若出现无法输入的情况，请检查输入法
        '''
        text1 = Label(setcomm,
            font_name = 'Times New Roman',
            font_size = 15,
            anchor_x = 'center',anchor_y = 'top',color=(7,7,14,200),width = 30,multiline = True)
        text1.position=120,180
        self.add(text1,1)

    def on_mouse_drag(self,x,y,dx,dy,button,modifiers):
        print("2====",x,y,dx,dy,button,modifiers)

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.font_item['font_size']=60
        self.font_item_selected['font_size']=100

        start_item=ImageMenuItem('IMG/23_1.png',self.on_start_item_callback)
        return_item=ImageMenuItem('IMG/23_3.png',self.on_return_item_callback)
        exit_item=ImageMenuItem('IMG/23_4.png',self.on_exit_item_callback)

        self.create_menu([start_item,return_item,exit_item],layout_strategy=fixedPositionMenuLayout([(700,380),(700,280),(700,180)]))

    def on_start_item_callback(self):
        print("on_start_item_callback")
        scene = Guess_game.create_scene()               #场景切换至游戏界面
        director.replace(scene)


    def on_return_item_callback(self):
        print("on_return_item_callback")
        scene = Guess_menu.Acreate_scene()              #场景切换至菜单界面
        director.replace(scene)

    def on_exit_item_callback(self):
        print("on_exit_item_callback")
        exit()

def create_scene():
    main_scene=Scene(Guess_rule())
    main_scene.add(MainMenu())
    return main_scene
