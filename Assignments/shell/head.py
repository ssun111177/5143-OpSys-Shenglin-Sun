import Input

#
def head(**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return

    file = Input.getFullFileName(kwargs['params'][0])
    
    if len(kwargs['params']) > 1 and str(kwargs['params'][1]).isdigit():
        noLines = int(kwargs['params'][1])
        noLines = noLines if noLines >= 0 else 5
    else:
        noLines = 5

    if file[0]:
        with open(file[1], 'r') as _file:
            x = 0
            for line in _file:
                if line.strip():
                    print (line.strip())
                    x += 1
                if x == noLines:
                    break
    else:
        print(file[1])