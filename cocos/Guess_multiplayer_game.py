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
import Guess_play
import socket

class Guess_menu(Layer):
    is_event_handler=True
    
    host = '127.0.0.1'
    port = 8888
    addr = (host,port)
    
    def __init__(self):
        super(Guess_menu,self).__init__()
        self.s_width,self.s_height=director.get_window_size()
        background = Sprite("IMG/图片1.png")
        background.position = self.s_width/2,self.s_height/2
        self.add(background,-2)
        title1  = Sprite("26.png")
        title1.position = 415,410
        self.add(title1,-1)

        lable1 = Sprite("IMG/22.png")
        lable1.position = 400,340
        self.add(lable1,-1)

        lable2 = Sprite("IMG/22_1.png")
        lable2.position = 0,305
        self.add(lable2,-1)

        lable = Label('INPUT ANSWER',
            font_name = 'Times New Roman',
            font_size = 32,
            anchor_x = 'center',anchor_y = 'top',color=(7,7,14,200))
        lable.position = 400,440
        self.add(lable,1)

        text3 = Label('Show your input',
            font_name = 'Times New Roman',
            font_size = 20,
            anchor_x = 'left',anchor_y = 'top',color=(7,7,14,200))
        text3.position=0,340
        self.add(text3,-1)

        self.text = Label('there',
            font_name = 'Times New Roman',
            font_size = 28,
            anchor_x = 'center',anchor_y = 'center',color=(7,7,14,200))
        self.text.position=400,360
        self.keys_pressed = ""
        self.update_text()
        self.add(self.text)

        self.text1 = Label('',
            font_name = 'Times New Roman',
            font_size = 25,
            anchor_x = 'left',anchor_y = 'top',color=(7,7,14,200))
        self.text1.position=0,300
        self.add(self.text1)
        self.anw = self.random_num()
        self.text2 = Label(self.anw,
            font_name = 'Times New Roman',
            font_size = 25,
            anchor_x = 'left',anchor_y = 'top',color=(7,7,14,200))
        self.text2.position = 0,450
        self.add(self.text2)

    def random_num(self):
        a=['0','1','2','3','4','5','6','7','8','9']
        answer = ''
        for i in range(4):
            num = random.choice(a)
            answer += num
            a.remove(num)
        return answer
       

    def update_text(self):
        # Update self.text
        self.text.element.text = self.keys_pressed

    def on_key_press(self, k, m):
        if k == pyglet.window.key.ENTER:
            print ("You Entered: {}".format(self.keys_pressed))
            # cocos.director.director.replace(FadeTransition(main_scene, 1))  # disabled for testing
            #cocos.director.director.scene.end()  # added for testing
            if self.keys_pressed.decode().isdecimal():
                if len(self.keys_pressed) == 4:
                    if self.keys_pressed == self.anw:
                        self.text1.element.text = self.keys_pressed+'  4A0B'
                    else:
                        B_COUNT = 0
                        for i in range(4):
                            for j in range(4):
                                if i!=j and self.anw[i] == self.keys_pressed[j]:
                                    B_COUNT+=1

                        A_COUNT = 0
                        for i in range(4):
                            if self.anw[i] == self.keys_pressed[i]:
                                A_COUNT +=1
                        self.text1.element.text = self.keys_pressed+'  '+str(A_COUNT)+'A'+str(B_COUNT)+'B'
                else:
                    self.text1.element.text = self.keys_pressed+u'  请输入四位数字序列'
                
            
           #self.text1.element.text = self.text1.element.text + '\n'+self.keys_pressed
            #self.text1.element.text = self.keys_pressed
            elif self.keys_pressed == 'SELECTANSWER':
                self.text1.element.text = str(self.anw)

            elif self.keys_pressed == 'RE':
                self.anw =self.random_num()
                self.text1.element.text = u"成功重置答案"
                self.text2.element.text = str(self.anw)                

            elif self.keys_pressed[0:10] == 'MODIFIEDTO':
                if self.keys_pressed[10:].decode().isdecimal():
                    if len(self.keys_pressed[10:]) ==4:
                        dict_sm = {}
                        for i in self.keys_pressed[10:]:
                            if i not in dict_sm:
                                dict_sm[i]=1
                            else:
                                dict_sm[i]+=1
                        if max(dict_sm.values()) > 1 :
                            self.text1.element.text = self.keys_pressed+u'  请输入正确序列'
                        else :
                            self.anw = self.keys_pressed[10:]
                            self.text1.element.text = u'成功修改数字序列'
                            self.text2.element.text = str(self.anw)
                            
                    else:
                        self.text1.element.text = self.keys_pressed+u'  请输入正确序列'
                else:
                    self.text1.element.text = self.keys_pressed+u'  请输入正确序列'
            else:
                self.text1.element.text = self.keys_pressed

            self.keys_pressed=''
            self.update_text()
            
        
        else:
            kk = pyglet.window.key.symbol_string(k)
            if kk == "SPACE":
                kk = " "
                #self.keys_pressed = self.keys_pressed + kk
            if kk == "BACKSPACE":
                self.keys_pressed = self.keys_pressed[:-1]
            if kk == "user_key(e5)":
                kk = " "

                '''
            else:
                # ignored_keys can obviously be expanded
                ignored_keys = ("LSHIFT", "RSHIFT", "LCTRL", "RCTRL", "LCOMMAND", 
                                "RCOMMAND", "LOPTION", "ROPTION")
                right_keys = ('NUM_0','NUM_1','NUM_2','NUM_3','NUM_4','NUM_5','NUM_6','NUM_7','NUM_8','NUM_9')

                if kk not in ignored_keys:
                    self.keys_pressed = self.keys_pressed + kk
                    '''
            right_keys = ('NUM_0','NUM_1','NUM_2','NUM_3','NUM_4','NUM_5','NUM_6','NUM_7','NUM_8','NUM_9')
            if kk in right_keys:
                self.keys_pressed = self.keys_pressed + kk[4]
            else:
                 # ignored_keys can obviously be expanded
                ignored_keys = ("LSHIFT", "RSHIFT", "LCTRL", "RCTRL", "LCOMMAND", 
                                "RCOMMAND", "LOPTION", "ROPTION","BACKSPACE","CAPSLOCK"," ","SPACE","LALT","TAB")
                if kk not in ignored_keys:
                    self.keys_pressed = self.keys_pressed + kk
                
            self.update_text()
        '''
        else:
            if k == 
            self.update_text()

'''


    def on_mouse_motion(self,x,y,dx,dy):
        print("1====",x,y,dx,dy)

    def on_mouse_drag(self,x,y,dx,dy,button,modifiers):
        print("2====",x,y,dx,dy,button,modifiers)

class MainMenu(Menu):
    def __init__(self):
        super(MainMenu,self).__init__()
        start_item=ImageMenuItem('11.png',self.on_start_item_callback)
        
        title_item=ImageMenuItem('1-2004121RF9.png',self.on_start_item_callback)
        self.create_menu([start_item,title_item],
            layout_strategy=fixedPositionMenuLayout([(780,435),(400,400)]))


    def on_start_item_callback(self):
        print("on_start_item_callback")
       # exit()

def create_scene():

    main_scene=Scene(Guess_menu())
    #main_scene.add(MainMenu())
    return main_scene
