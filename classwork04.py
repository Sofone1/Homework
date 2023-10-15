mylist = [1, 2, 3, 4, 5]
# elementis damateba
mylist.append(6)
print(mylist)

print(mylist[1: 3]) # gamoitanos indeqsit 1-3
print(mylist[:3]) # gamoitalos yvelaferi indeqsit 3-mde
print(mylist[3:]) # gamoitanos yvelaferi indeqsi 3-is shemdeg
mylist.sort(reverse = True)
print(mylist) # gamoitanos shebrunebulad yvelaferi

myl2 = ['red', 'blue', 'green', 'yellow']
if myl2[0] == 'red':
    print('Yes')
if 'red' in myl2:
    print('Yes')
else:
    print('No')

result = 'red' in myl2
print(result)

myl3 = ['brown', 'purple']
result2 = myl2.append(myl3)
print(result2)
myl2.append(myl3)
print(myl2)

myl4 = [1, 2, 3, 4, 5]
myl4.pop(2)
print(myl4)
myl4.remove(5)
print(myl4)
myl4.clear()
print(myl4)

myl5 = [1, 2, 3, 4, 5, 5, 5, 5]
counted = myl5.count(5)
print(counted)

myl6 = [1, 7, 4, 3, 6, 8, 10]
myl6.sort()
print(myl6)

word = 'sophio'
word_r = list(word)
print(word_r)

for i in range(1, 11):
    print(i)

res = list(range(-5, 6))
print(res)

big_word = 'red car enters garage'
result_big_word = big_word.split()
print(result_big_word)

big_word2 = 'blue-car-enters-the-house'
symbol = '-'
result_big_word2 = big_word2.split(symbol)
print(result_big_word2)

words3 = ['hi', 'hello', 'hola']
symbol2 = ' '
result3 = symbol2.join(words3)
print(result3)
