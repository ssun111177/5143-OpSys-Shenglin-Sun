import Input, cat

#
def sort(**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return

    fileItems = []
    fileItems = cat.cat(False,**kwargs).split('\n')

    fileItems.sort()

    for item in fileItems:
        print(item)