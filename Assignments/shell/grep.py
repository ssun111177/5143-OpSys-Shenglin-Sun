import Input

#search a file(s) files for keywords and print lines where pattern is found
def grep(**kwargs):
    if Input.isParamsListEmpty(kwargs['params'], 2):
        return
    
    flags = Input.isFlagsListEmpty(kwargs['flags'])

    lines = []
    keywd = kwargs['params'][0].strip('\'')

    for fileName in kwargs['params'][1:]:
        file = Input.getFullFileName(fileName)

        if file[0]:
            with open(file[1], 'r') as _file:
                for line in _file:
                    if line.strip() and keywd in line.strip().lower():
                        lines.append(line.strip())
            
            if len(lines) != 0:
                if flags:
                    for line in lines:
                        print(line)
                else:
                    if kwargs['flags'][0] == '-l':
                        print('\'' + keywd + '\'' + ' was found in \'' + file[1] + '\'\n')
                    else:
                        print('\'' + kwargs['flags'][0] + '\'' + ' is not a recognized flag\n')
            else:
                print('\'' + keywd + '\'' + ' was not found in \'' + file[1] + '\'\n')
        else:
            print(file[1])
            break