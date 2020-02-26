import Input, os

#
def mkdir(**kwargs):
    if len(kwargs['params']) == 0:
        print('Directory name not provided')
        return

    directory = ' '.join(kwargs['params'])

    directoryPath = os.path.join(os.getcwd(),directory)

    if os.path.isdir(directoryPath):
        print('Directory already exists')
        return
    else:
        os.mkdir(directoryPath)

    print('"' + directory + '" has been created.')