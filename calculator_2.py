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
