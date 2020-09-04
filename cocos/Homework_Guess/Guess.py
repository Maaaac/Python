#coding:utf-8
import cocos
import pyglet
from cocos.actions import *
from cocos.director import director
from cocos.layer import Layer
from cocos.menu import *
from cocos.scene import Scene
from cocos.scenes.transitions import *
from cocos.sprite import Sprite

import Guess_menu


class loading(Layer):
    is_event_handler=True
    def __init__(self):
        super(Layer,self).__init__()
        self.s_width,self.s_height=director.get_window_size()
        background = Sprite("IMG/IMG1_1.jpg")
        background.position = self.s_width//2,self.s_height//2
        self.add(background,-2)

        title_lable = cocos.text.Label('Guess Game',font_name='Times New Roman',font_size=32,anchor_x='center',anchor_y='center',color=(7,7,14,200))
        title_lable.position = self.s_width//2,self.s_height//2
        self.add(title_lable,1)
        
    def on_mouse_motion(self,x,y,dx,dy):
        print("1====",x,y,dx,dy)

    def on_mouse_drag(self,x,y,dx,dy,button,modifiers):
        print("2====",x,y,dx,dy,button,modifiers)

    def on_mouse_press(self,x,y,button,modifiers):
        print(x,y,button,modifiers)
        scene = Guess_menu.Acreate_scene()              #场景切换至菜单界面
        director.replace(scene)


    def on_key_press(self,key,modifiers):
        print("keyboard press",key," === ",modifiers)
        if key == pyglet.window.key.SPACE:
            print("你按下了空格键")

    def on_key_release(self,key,modifiers):
        print("keyboard release",key," === ",modifiers)
        if key == pyglet.window.key.SPACE:
            print("你释放了空格键")
        if key == pyglet.window.key.P:
            print("P")

if __name__ == "__main__":
    director.init(width=800,height=450,caption="Guess")
    main_scene=Scene(loading())
    #main_scene.add(MainMenu())
    director.run(main_scene)
