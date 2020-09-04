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
from cocos.text import *
import random

def random_num():
    a=['0','1','2','3','4','5','6','7','8','9']
    answer = ''
    for i in range(4):
        num = random.choice(a)
        answer += num
    return answer
        

'''
if __name__ == "__main__":
    print(random_num())
    '''