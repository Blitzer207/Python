# -*- coding: utf-8 -*-

import sys
from socket import *

# python3 port_scan.py <host> <start_port>-<end_port>
host=input("IP Address: ")
start_port=int(input("Start port: "))
end_port=int(input("End port: "))
#host = sys.argv[1]
#portstrs = sys.argv[2].split('-')

#start_port = int(portstrs[0])
#end_port = int(portstrs[1])

target_ip = gethostbyname(host)
opened_ports = []

for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM) # 创建一个socket对象

#设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
    # 一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
    sock.settimeout(10)

##主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），
    # 如果连接出错，返回socket.error错误。扩展版本,出错时返回出错码,而不是抛出异常
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)

print("Opened ports:")

for i in opened_ports:
    print(i)