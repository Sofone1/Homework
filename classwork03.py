main_list = [5, 7, 8, 2]
main_list.sort()
print(main_list)
main_list.sort(reverse = True)
print(main_list)
main_list.sort(reverse = False)
print(main_list)

str_list = ['hi', 'hello', 'holla', 'bonjorno', 'hey', 'bye']
str_list.sort()
print(str_list)
str_list.sort(reverse = True)
print(str_list)

for i in range(1, 11):
    print(i)

for i in reversed(range(1, 11)):
    print(i)

names = ['natalia', 'sophio', 'giorgi']
for i in names:
    if i == 'sophio':
        print(i)

for i in range(1, 6):
    if i == 4:
        break
    print(i) #ar iprintebaa T-T #daiprintaaaa :D wohoo!!!
