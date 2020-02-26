import Input, os


#
def ls(**kwargs):
    for items in os.listdir(os.getcwd()):
        print (items)
        
#future implementation
# def ls(**kwargs):
#     directoryItems = []
#     directoryItemsFormatted = ''
#     for items in os.listdir(os.getcwd()):
#         directoryItems.append(items)
        
#     directoryItems.sort(key = len,reverse = True)

#     for items in directoryItems:
#         directoryItemsFormatted += items + '\t'

    #for x in range(5):
    #print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))
    #print (directoryItemsFormatted)
