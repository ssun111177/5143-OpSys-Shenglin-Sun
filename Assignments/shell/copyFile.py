import Input, os
import cat

def copyFile(**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return
    
    fileList = kwargs['params']

    file = Input.getFullFileName(fileList[0])
    if not file[0]:
        print(file[1])
        return

    if len(fileList) > 2:
        print('Too many files provided\n')
        return
    
    kwargs['params'] = [fileList[0]]

    cwd = Input.getCwd(fileList[1])

    if os.path.exists(cwd):
        newFile = open(fileList[1],'w')
        newFile.write(cat.cat(False,**kwargs))
        newFile.close()
    else:
        print(fileList[1] + ' : path doesn''t exist\n')
        return

    print(str(fileList[1]) + ' has been created\n')
