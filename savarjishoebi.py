#1
message = "What's up, Tim?"
print(message)

#2
numbers = input('write 3 numbers: ')
sym = ','
nnumbers = numbers.split(sym)
print((int(nnumbers[0]) + int(nnumbers[1]) + int(nnumbers[2])) / 3)

#3
l5 = []
for i in range(20, 126):
    if i % 5 == 0:
        l5.append(i)
print(l5)

#4
words = input("write 10 items: ")
l1 = words.split(sym)
print(l1)

#5
numb = input("write some number: ")
lword = list(numb)
print(lword[0])

#6
x = 0
for i in range(1, 101):
    if i % 2 == 0:
        x += i
print(x)

#7
set1 = {10, 20, 30, 40, 50}
set1.update([60, 70])
set1.remove(10)
x = 0
for i in list(set1):
    print(i)
    x += 1
print(x)

#8
set2 = set([])
jami = 0
for i in range(1, 101):
    if i % 5 == 0:
        set2.add(i**3)
        jami += i**3
print(jami / len(list(set2)))

#9
nnnumbers = input('write 3 numbers: ')
sym = ','
numb = [int(i) for i in nnnumbers.split(sym)]
import random
min1 = int(numb[random.randint(0, 2)])
for i in numb:
    if i < min1:
        min1 = i
print(min1) #gza - 1
print(min(numb)) #gza - 2

#10
mnumber = input('write any number: ')
lmnumber = list(mnumber)
print(lmnumber[-1]) #gza - 1

x = 0
while x < len(lmnumber):
    if x == len(lmnumber) - 1:
        print(lmnumber[x]) #gza - 2
    x += 1