# coding=utf-8
import threading
import socket
import time
import random
def func(cnn):
    def random_num():             #序列生成函数
        a=['0','1','2','3','4','5','6','7','8','9']
        num = ''
        for i in range(4):
            m=random.choice(a)
            num += m
            a.remove(m)
        return num
    sq = random_num()
    dict_count = {}
    while True:
        try:
            print ("waiting for message...")
            request = cnn.recv(1024)

            request = request.decode('utf-8')
            print(u'接收到来自客户端'+str(cnn.getpeername())+u'的信息，信息内容为：'+request)

            
            if str(cnn.getpeername()) in dict_count.keys():                     #以字典的形式保存每个用户的最近一次游戏成绩（猜的次数）
                dict_count[str(cnn.getpeername())]+=1
            else:
                dict_count[str(cnn.getpeername())]=0
        
            return_msg = ''
            if request.isdecimal():
                A_COUNT = 0
                B_COUNT = 0
                if len(request) == 4:
                    for i in range(4):
                        if request[i] == sq[i]:
                            A_COUNT += 1
                        else:
                            for j in range(4):
                                if request[i] == sq[j] and i!=j:
                                    B_COUNT += 1   
                    return_num = str(A_COUNT)+'A'+str(B_COUNT)+'B'

                    if return_num == '4A0B':

                        for key in dict_count.items():
                            if dict_count[str(cnn.getpeername())] <= key:                   #判断胜负（若为单人自动判断为win）
                                i = 1         
                            else:
                                i = -1
                                break
                        if i == 1:
                            return_msg = return_num + " and you win , your number of time is "+str(dict_count[str(cnn.getpeername())])
                            cnn.send(return_msg.encode('utf-8'))
                        elif i == -1:
                            return_msg = return_num + " but you lose , your number of time is "+str(dict_count[str(cnn.getpeername())])
                            cnn.send(return_msg.encode('utf-8'))
                        sq = random_num()
                        print(dict_count)
                    else:
                        cnn.send(return_num.encode('utf-8'))

                else:     
                    return_msg = u'请输入正确的数字序列'
                    cnn.send(return_msg.encode('utf-8'))      
            
                print(str(A_COUNT)+'A'+str(B_COUNT)+'B')
            #指令语句
            elif request == 'RE':
                sq = random_num()
                dict_count[str(cnn.getpeername())]=0
                print('ask resert sq , successful re')
                cnn.send("successful re".encode('utf-8'))
            
            elif request == 'SELECTANSWER':
                cnn.send(sq.encode('UTF-8'))
                print('ask show answer')
            
            elif request[0:10] == 'MODIFIEDTO':
                if request[10:].isdecimal():
                    if len(request[10:]) == 4:
                        sq == request[10:]
                        cnn.send("successful modified".encode('UTF-8'))
                    else:
                        cnn.send("Plase input right sq".encode('UTF-8'))
                cnn.send("Plase input right sq".encode('UTF-8'))

            else:
                print("input wrong command".encode('UTF-8'))
                cnn.send('input wrong command'.encode('UTF-8'))            #非法输入
        except Exception as e:                                              #检测异常，直接抛出，示意玩家断线
            print("玩家已断线")
            break


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))
    s.listen(5)

    while True:
        #print("等待客户端接入中")
        cnn, addr = s.accept()
        th = threading.Thread(target=func,args=(cnn,))
        th.start()