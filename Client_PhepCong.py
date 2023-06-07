# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:26:07 2023

@author: ADMIN
"""


import socket

if __name__=='__main__':
    host = 'localhost'
    port = 9050
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host,port))
    data = sk.recv(1024)
    print(data.decode('utf-8'))
    while True:
        data = input('Enter message:')
        if data =='=':
            sk.send(data.encode('utf-8'))
            # Nhận kết quả
            data = sk.recv(1024)
            print(data.decode('utf-8'))
            sk.close()
            break
        sk.send(data.encode('utf-8'))
        #data = sk.recv(1024)
        #print(data.decode('utf-8'))
        