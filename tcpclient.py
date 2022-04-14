# coding=utf-8


import socket


host = "192.168.206.1"
port = 8000

clientsocket = socket.socket()  #socket的默认参数为socket.AF_INET, socket.SOCK_STREAM
clientsocket.connect((host, port))


while True:
    data = clientsocket.recv(1020).decode("UTF-8")  # 用UTF-8对接收到的信息进行解码
    print("receive data:",data)

    while True:
        userinput = input("请输入需要传输的数据，输入close断开连接")

        if len(userinput) == 0:
            print("command error")
            pass
        else:
            clientsocket.send(userinput.encode("UTF-8"))

        if userinput == 'close':
            clientsocket.close()
            print("socket is closed")
            break

#客户端的接收和发送，做成不同线程？？？待尝试

clientsocket.close()