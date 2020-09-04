#coding=utf-8
import cocos

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld,self).__init__()  #调用父类构造方法
        #cocos.layer.Layer.__init__()      #构造的另一个方法
        #创建标签
        label=cocos.text.Label('Hello,World',font_name='Times New Roman',font_size=32,anchor_x='center',anchor_y='center')
        #获取屏幕大小
        width,height=cocos.director.director.get_window_size()
        label.position=width/2,height/2
        label1=cocos.text.Label('Hello,World',font_name='Times New Roman',font_size=48,anchor_x='center',anchor_y='center')
        label1.position=width/2,height/2
        #将标签添加进层
        self.add(label)
        self.add(label1,1)
        

if __name__=='__main__':
    cocos.director.director.init()
    hw_layer=HelloWorld()
    main_scene=cocos.scene.Scene(hw_layer)
    cocos.director.director.run(main_scene)#开始运行
