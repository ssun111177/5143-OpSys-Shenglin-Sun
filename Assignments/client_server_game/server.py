# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:08:26 2020

@author: sun
the server fille is using for holding the game while clients connecting with it
basicly how the code working is running the game in the server.py, client.py send required input value,
then server.py receive the value from client.py and use them to keep running the game and send the output sentence to client.py
"""

import socket
#import threading
#import game
import random

Host = socket.gethostbyname
Port = 1234
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host,Port))
s.listen(3)#set the maxium connected number
socks=[]
clients,address=s.accept()
while 1:
    INT_MAX = 20
    #print ("Guessing number")
    n = random.randint(1,2)
    s = "nil"
    if n==1:
        s = "H"
    else:
        s = "L"
    level = clients.recv(256)#give the value that received from client to level
    msg = ""
    if level == s:
        msg="that's right, it's "+s
    else:
        msg="that's wrong, it's "+s
        
    clients.send(msg.encode("utf-8"))#send the L/H guessing response to client
    
    if n ==1:#for the case of H, do the guessing between 1 to INT_MAX
        msg0="guess a number between 1 to "+str(INT_MAX)
        clients.send(msg0.encode("utf-8"))
        random_num = random.randint(1,INT_MAX)
        time = 0
        while time < 20:
            num = clients.recv(512)#receive the input number from client.py and give the value to num
            if num == random_num:
                break;#which means the guessing is correct, break the loop
            elif num < random_num:
                msg1="-1."
            else:
                msg1="1."
            time = time+1
            clients.send(msg1.encode("utf-8"))#if it's not correct, output -1/1 to client.py
        msg1="0."
        clients.send(msg1.encode("utf-8"))#if it's correct, output 0 to client.py

            
    else:#for the case of L, do the guessing between 0 to INT_MAX-1
        msg0="guess a number between 0 to "+str(INT_MAX-1)# same as above, using same pass and receive as above.
        clients.send(msg0.encode("utf-8"))
        random_num = random.randint(0,INT_MAX-1)
        time = 0
        while time < 20:
            num = clients.recv(512)
            if num == random_num:
                break;
            elif num < random_num:
                msg1="-1."
            else:
                msg1="1."
            time = time+1
            clients.send(msg1.encode("utf-8"))
        msg1="0."
        clients.send(msg1.encode("utf-8"))
s.close
    





