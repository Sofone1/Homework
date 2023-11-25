#1
list1 = [1, 2, 3, 2, 4, 3, 4, 4, 3]
set1 = set(list1)
list2 = list(set1)
x = 0
dic = {}
while x < len(list2):
    dic[list2[x]] = list1.count(list2[x])
    x += 1
print(dic)

#2
list3 = [1, 2, 3, 6, 8, 8, 9, 10]
set3 = set(list3)
print(set1 & set3)

#3
list5 = []
for i in list1:
    if i not in list5:
        list5.append(i)
print(list5)

#4
print(dic)
list4 = []
for x in dic:
    list4.append(dic[x])
jami = 0
for i in list4:
    jami += i
print(jami)

#5
vowel = ['a', 'e', 'i', 'o', 'u']
word = input('any word: ')
lword = list(word)
vcount = 0
for i in lword:
    if i == 'a':
        vcount += 1
    if i == 'e':
        vcount +=1
    if i == 'i':
        vcount +=1
    if i == 'o':
        vcount +=1
    if i == 'u':
        vcount +=1
print(vcount)

#6
word1 = 'sophio'
lword1 = list(word1)
z = 0
dic2 = {}
while z < len(lword1):
    dic2[lword1[z]] = lword1.count(lword1[z])
    z += 1
print(dic2)

#7
mlist = [12, 21, 32, 11]
udidesi = 0
for i in mlist:
    if i > udidesi:
        udidesi = i
print(udidesi)

#8
lulist = [1, 2, 3, 45, 4, 8, 6, 7]
lujami = 0
x = 0
while x < len(lulist):
    if lulist[x] % 2 == 0:
        lujami += lulist[x]
    x += 1
print(lujami)

#9
x = 1
x2 = []
while x < 11:
    x2.append(x**2)
    x += 1
print(x2)