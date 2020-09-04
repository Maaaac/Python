#coding:utf-8
import cocos
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.menu import *
import pyglet

class SettingLayer(Layer):
    is_event_handler=True

    def __init__(self):
        super(SettingLayer,self).__init__()
        self.s_width,self.s_heigt = director.get_window_size()
        background = Sprite("4.png")
        background.position = self.s_width//2,self.s_heigt//2
        self.add(background,-1)

def create_scene():
    scene=Scene(SettingLayer())
    return scene