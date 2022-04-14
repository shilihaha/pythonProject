# coding=utf-8

import socket

#socket.AF_INET, socket.SOCK_STREAM，分别代表ipv4地址族和TCP流
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
print("host IP",host)
port = 8000

serversocket.bind((host,port))
serversocket.listen(5)  #最多可以可以接受5个连接请求

while True:
    conn,addr = serversocket.accept()
    print("received",addr)
    conn.send('welcome to visit'.encode("UTF-8"))

    while True:
        data = conn.recv(1024).decode("UTF-8")
        if not data:
            pass
        else:
            print(data)

        if data == 'close':
            print("End of this connection")
            conn.close()
            break

        if len(data) == 0:
            print("connect error")
            conn.close()
            break

        #userdata = input("请输入要回复的数据，按回车跳过")
        #if len(userdata) == 0:
            #pass
        #服务器端，根据指令做出不同动作，待改进。。。

#服务器做成可以多客户端连接。。。待完成

conn.close()
