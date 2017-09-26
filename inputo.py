print('THE INPUTO :D')

list = []
print('Please choose to insert, delete, update or list')
print('this is to make a list\n')

conti='y'
while conti == 'y' :
    insertcomand=input('What to do?')
    if insertcomand.lower()  == 'insert':
        data= input('Insert your data here :')
        list.append(data)
        print(list)
    elif insertcomand.lower() == 'delete':
        list.pop()
        print(list)
    elif insertcomand.lower() == 'update':
        print(list)
        data = int(input('which one got updated (in number start with 0):'))
        updated = input('what need to be change :')
        list[data] = updated
        print(list)
    elif insertcomand.lower() == 'list':
        print(list)
    else :
        print('Error, please try again !!')
    conti = input('Do you wish to continue (y/n) ?')
print('Thank you for using inputo :D')
