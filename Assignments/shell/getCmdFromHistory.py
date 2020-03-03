import Input, os
import cat


def getCmdFromHistory(cmdNum):
    commands = []
    with open("historyList.txt",'r') as readHistoryFile:
        for command in readHistoryFile.readlines():
            commands.append(command)
    
    commandNum = int(cmdNum.split('!')[1])

    commandToRun = commands[commandNum].split(':')[1].strip()
    return commandToRun
