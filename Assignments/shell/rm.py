import Input, os

#
def rm(**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return

    file = Input.getFullFileName(kwargs['params'][0])

    if file[0]:
        filePath = os.getcwd() + '\\'+ file[1]
    else:
        print(file[1])
        return
    
    print('deleting file...........')
    os.remove(filePath)
    print(file[1] + ' successfully deleted!')