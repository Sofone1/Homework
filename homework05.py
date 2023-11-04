# N6
dic1 = {}
dic1.update({
    'FirstName': 'Jane',
    'LastName': 'Doe',
    'hobbies': ['runnung', 'skydiving', 'singing'],
    'age': 35,
    'children':[
    {
        'firstname': 'Alice',
        'age': 6
    },
    {
        'firstname': 'Bob',
            'age': 8
    }]})
print(dic1.get('FirstName'), dic1.get('LastName'), dic1.get('age'), dic1.get('children'))


# N8
set1 = set([0, 1, 2, 3, 4])
set1.update([5, 6, 7])
set1.discard(0)
set1.pop()
print(set1)
for i in set1:
    print(i)
print(len(set1))

# N9 - I
set2 = set(['green', 'blue'])
set3 = set(['blue', 'yellow'])
list4 = list(set2) + (list(set3))
print(set(list4)) # gaertianeba
for x in list4: #tanakveta
    if list4.count(x) > 1:
        print(x)
        list4.remove(x)
list4 = list(set2) + (list(set3))
for x in list4: # sxvaoba
    if list4.count(x) > 1:
        set2.discard(x)
        print(set2)
        list4.remove(x)
set2 = set(['green', 'blue'])
set3 = set(['blue', 'yellow'])
list4 = list(set2) + (list(set3))
for x in list4: # simetriuli sxvaoba
    if list4.count(x) > 1:
        set5 = set(list4)
        set5.discard(x)
        print(set5)
    break

# N9 - II
set2 = set(['green', 'blue'])
set3 = set(['blue', 'yellow'])
print(set2 | set3) #gaertianeba
print(set2 & set3) # tanakveta
print(set2 - set3) #sxvaoba
print(set2 ^ set3) #simetriuli sxvaoba

# N10
set6 = set([1, 3, 2, 5, 4, 6, 7, 12, 10])
x = 0
largest = list(set6)[0]
smallest = list(set6)[0]
while x < len(list(set6)):
    if (list(set6)[x] > largest):
        largest = list(set6)[x]
    elif (list(set6)[x] < smallest):
        smallest = list(set6)[x]
    x += 1
print('largest:', largest)
print('smallest:', smallest)

# N11
nlist = list(input('write anything: '))
nset = set(nlist)
print(nset)

# N12
in1 = list(input('write anything: '))
in2 = list(input('write anything: '))
in3 = in1 + in2
in4 = []
for x in in3:
    if in3.count(x) > 1:
        in4.append(x)
        while x in in3:
            in3.remove(x)
print(in4)