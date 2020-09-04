
import cocos
 
 
#背景层
class Game_Setting(cocos.layer.Layer):
    def __init__(self):
        super(Game_Setting,self).__init__()
        d_width, d_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite('IMG.jpg')
        background.position = d_width // 2, d_height // 2
        self.add(background)
 
 
#自定义菜单类
class main_menu(cocos.menu.Menu):
    def __init__(self):
        super(main_menu, self).__init__()
 
        # 也可以改变图片项的大小
        # 改变字体
        self.font_item['font_size'] = 66
        # 选中时
        self.font_item_selected['font_size'] = 66
        #改变颜色 rgba
        self.font_item['color'] = (255,255,255,25)
        # 选中时
        self.font_item_selected['color'] = (215,255,255,255)
 
        ok = cocos.menu.ImageMenuItem('1.png', self.ok_callback)
        #创建菜单（添加项的列表，自定义布局位置）
        self.create_menu([ok],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout([(560,130)]),
                         selected_effect=cocos.menu.zoom_in(),
                         unselected_effect=cocos.menu.zoom_out())
 
 
    def ok_callback(self):
        cocos.director.director.pop()
 
def create():
    #将背景层  添加到场景
    bg=Game_Setting()
    main_scence=cocos.scene.Scene(bg)
    #添加菜单
    mainmenu=main_menu()
    main_scence.add(mainmenu)
    return main_scence
