import Input

#
def tail(**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return

    file = Input.getFullFileName(kwargs['params'][0])
    
    if len(kwargs['params']) > 1 and str(kwargs['params'][1]).isdigit():
        noLines = int(kwargs['params'][1])
        noLines = noLines if noLines >= 0 else 5
    else:
        noLines = 5

    if file[0]:
        lines = []
        lineCounter = 0
        with open(file[1], 'r') as _file:
            for line in _file:
                if line.strip():
                    lines.append(line.strip())
                    lineCounter += 1
        lines = lines[lineCounter - noLines:]  

        for lastLines in lines:
            print (lastLines)
    else:
        print(file[1])