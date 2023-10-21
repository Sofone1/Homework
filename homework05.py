# listi romelic sheicavs pirvel 10 luw ricxvs
list1 = []
x = 2
while x <= 20:
    list1.append(x)
    x+=2
print(list1)

# listshi yvela elementis jami
list2 = [5, 15, 25, 35]
total = sum(list2)
print(total)

# yoveli mesame elementis amoprintva listidan
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
z = 2
thirdl = []
while z <= (len(list3)-1): # len(list3)-s minus 1 radgan indeqsi 1-it naklebia elementebis raodenobaze
    thirdl.append(list3[z])
    z += 3
print(thirdl)

# duplikati elementebis washla listidan
list4 = [1, 2, 3, 4, 5, 5, 6, 6, 6]
set4 = set(list4)
print(list(set4))

# datvla listshi titoeuli elementis raodenobis da dictionary-shi dabruneba
list5 = [8, 12, 3, 19, 7, 1, 3, 12, 8, 19, 1, 5, 6, 7, 19]
set5 = set(list5)
list6 = list(set5)
x = 0
dict = {

}
while x <= len(list6)-1:
    dict[list6[x]] = list5.count(list6[x])
    x += 1
print(dict)
