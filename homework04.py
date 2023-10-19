# amoprintos 1-6 magram shewydes 5-ze
for i in range(1, 6):
    print(i)
    if i == 5:
        break

# carieli list, romelsac emateba ricxvebi 1-5
mylist = []
x = 1
while x < 6:
    mylist.append(x)
    x += 1
print(mylist)

# chawerili 3 ricxvidan, amoprintos umciresi
list1 = (input('Write 3 numbers (separate with ,): '))
symbol = ','
list2 = list1.split(symbol)
list3 = [int(list2[0]), int(list2[1]), int(list2[2])]
list3.sort()
print(list3[0])

# nebismieri ricxvis shetanis shemdeg unda amoiprintos: dadebitia, uatyofiti tu 0
number = int(input('Any number: '))
if number == 0:
    print('Number is equal to 0')
elif number < 0:
    print('Number is negative')
else:
    print('Number is positive')

# tu ori chawerili ricxvi metia 10-ze, amoprintos mati aritmetikuli, xolo tu orive naklebia, mati namravli
list4 = (input('Write 2 numbers (separate with ,): '))
symbol = ','
list5 = list4.split(symbol)
list6 = [int(list5[0]), int(list5[1])]
if list6[0] < 10 and list6[1] < 10:
    print(list6[0] * list6[1])
elif list6[0] > 10 and list6[1] > 10:
    print((list6[0] + list6[1]) / 2)
else:
    print('Error!')

# chawerili ricxvis latinuri asoebit aghnishvna
number2 = int(input('Write any number: '))
if number2 in range(0, 40):
    print('Failed')
elif number2 in range(41, 50):
    print('FX')
elif number2 in range(51, 60):
    print('E')
elif number2 in range(61, 70):
    print('D')
elif number2 in range(71, 80):
    print('C')
elif number2 in range(81, 90):
    print('B')
elif number2 in range(91, 100):
    print('A')
else:
    print('Error')
