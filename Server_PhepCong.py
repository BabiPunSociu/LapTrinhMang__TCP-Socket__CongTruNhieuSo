# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:26:15 2023

@author: ADMIN
"""

import socket
a = [] # 1+2-3=
chuoi = ""
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('localhost',9050))
sk.listen(5)
client_sk, client_addr = sk.accept()
client_sk.send('Haluuu Pún'.encode('utf-8'))
while True:
    data = client_sk.recv(1024)
    a.append(data.decode('utf-8'))
    chuoi += data.decode('utf-8')
    print(*a)
    # Nếu đóng server
    if data.decode('utf-8') == '=':
        ketqua = 0
        ind= -1
        for i in a: # Tính kết quả
            ind = ind + 1
            try:
                b = int(i)
                ketqua += b
            except ValueError:
                if i == '+':
                    continue
                if i == '-':
                    a[ind+1] = '-'+a[ind+1]
        chuoi += str(ketqua)
        client_sk.send(chuoi.encode('utf-8'))
        client_sk.close()
        break
    
    