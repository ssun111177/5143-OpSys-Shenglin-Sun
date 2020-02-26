#import sys

import Input,os
path = os.getcwd()
#def getname(path):
def ls(**kwargs):
    if os.path.isdir(path):
        filder = os.listdir(path)
        print(filder)
        #return filder
    else:
        print("wrong path")
        exit()
        
    
    
