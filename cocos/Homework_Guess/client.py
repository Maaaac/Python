# -*- coding:utf-8 -*-
# coding:utf-8

from socket import *
import time

client = socket(AF_INET, SOCK_STREAM)  
client.connect(('127.0.0.1', 8888))  
print(client.getpeername())

print(client.getsockname())
print("——————————————————————————————————————————")
print("----------------Guess Game----------------")
print("----------请输入四位数字的序列------------")
print("——————————————————————————————————————————")
print("|--------------系统特殊指令--------------|")
print("|---------查询答案:SELECTANSWER----------|")
print("|--------修改序列:MODIFIEDTOXXXX---------|")
print("|---------------重置序列:RE--------------|")
print("|----------------退出:over---------------|")

while True:

    msg = raw_input("请输入答案或指令:")
    if msg =='':
        print("请输入答案或指令")
    else:

        if msg == 'over':
            client.close()
            exit()
        else:
            client.send(msg.encode('UTF-8'))
            #print("1")
            #data,addr = client.recvfrom(1024)
            #data=data.decode('utf-8')
            data = client.recv(1024)
            print (data.decode('utf-8'))
            if data[0:4] == '4A0B':                                                 #当输入正确答案时，询问玩家是否继续
                yn = raw_input("victory   play continue?(Y/N):")
                if yn == 'Y':
                    pass
                else:
                    exit()
            continue
    
client.close()    
