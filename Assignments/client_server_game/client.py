# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:08:56 2020

@author: sun
client.py will recive ouput message from server.py, all the input value in client will be pass to server as the input value in server.py's algorithm
"""

import socket


Host = socket.gethostbyname
Port = 1234

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect((Host,Port))
address=(Host,Port)

while 1:
    level = input("first guess is this a L or H:")
    c.send(level.encode("utf-8"))#send the L/H guessing to the server
    msg=c.recv(256)#receive the L/H guessing response from server
    print(msg)#output the message of guessing response
    msg0=c.recv(128)#receive the starting word from the server
    print(msg0)
    time = 0
    while time < 20:#paring for the two while in if systems, because if system is either one of each case, so client only need one running
        num = int(input("please type your number:"))
        c.send(num.encode("utf-8"))#send the reall guess game's ansers to server
        msg1=c.recv(512)#receive the reall guess game's ansers' response from server
        print(msg1)
        time=time+1


c.close()