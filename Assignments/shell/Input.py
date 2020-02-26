import sys, os
#from tabulate import tabulate

def getname(path):
    if os.path.isdir(path): 
        folder = os.path.basename(path) #+ ["    "] # use .listdir to list folder's name of current address
        print('Directory name : ' + folder)

    else:
        print("wrong path")
        exit()

#get the fullname of the file (basically adds the extension to it)
def getFullFileName(file):
    for items in os.listdir(os.getcwd()):
        if file == items.lower() or file == items.split('.')[0].lower():
            ffn = [True,items]
            return ffn
        else:
            ffn = [False,'File(s) not found\n']
    return ffn

def isParamsListEmpty(paramsList,minNumParams=1):
    if paramsList == [] or len(paramsList) < minNumParams:
        print('file name not provided.')
        return True

def isFlagsListEmpty(flagsList):
    if flagsList == []:
        print('flag(s) not provided.')
        return True
    else:
        return False


def recordHistory(command):
    with open("historyList.txt") as readHistory:
        cmdHistory = readHistory.readlines()
    lastCommand = cmdHistory[-1]

    lastCommandNumber = int(lastCommand.split(':')[0])
    lastCommandNumber += 1

    writeToHistory = open("historyList.txt","a")
    writeToHistory.writelines(str(lastCommandNumber) + ':' + command + '\n')
    writeToHistory.close()