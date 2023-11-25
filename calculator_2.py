action = input('write numbers and operation you want to make (+, -, *, /, ^): ')
laction = list(action)
for i in laction:
    if i == '+':
        number1 = int(action.split('+')[0])
        number2 = int(action.split('+')[1])
        print(int(number1) + int(number2))
    elif i == '-':
        number1 = int(action.split('-')[0])
        number2 = int(action.split('-')[1]) 
        print(int(number1) - int(number2))
    elif i == '*':
        number1 = int(action.split('*')[0])
        number2 = int(action.split('*')[1]) 
        print(int(number1) * int(number2))
    elif i == '/':
        number1 = int(action.split('/')[0])
        number2 = int(action.split('/')[1]) 
        print(int(number1) / int(number2))
    elif i == '^':
        number1 = int(action.split('^')[0])
        number2 = int(action.split('^')[1]) 
        print(int(number1)**int(number2))

# list1 = [1, 2, 3, 4, 5, 6]
# x = 0
# while x < len(list1) - 1:
#     nnumber = str(list1[x]) + str(list1[x+1])
#     x+=1
#     for n in list(nnumber):
#         if n == 3:
#             print(nnumber)
#         break
#     print(nnumber)