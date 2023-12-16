#1
class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    
    def far(self):
        fa = self.width * self.length
        return fa
    def peri(self):
        pe = 2*(self.width + self.length)
        return pe

obj1 = rectangle(3, 5)
print(obj1.peri())
print(obj1.far())

#2
class car:
    def __init__(self, color, model, makeYear, fuelType):
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType
    
    def sell(self):
        car = [self.color, self.model, self.makeYear, self.fuelType]
        return f"you want to sell this car: {' '.join(car)}?"
    def buy(self):
        car = [self.color, self.model, self.makeYear, self.fuelType]
        return f"you want to buy this car: {' '.join(car)}?"


car1 = car('red', 'toyota', '2015', 'gas')
car2 = car('aquamarine', 'bmw', '1997', 'gas')
car3 = car('rose', 'ferrari', '2020', 'gas')
print(car1.sell())
print(car2.sell())
print(car3.sell())
print(car1.buy())
print(car2.buy())
print(car3.buy())

#3
class dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

dog1 = dog('West highland white terrier', 'small', '2 years', 'white')
dog2 = dog('korgi', 'medium', '3 months', 'orange/white')
dog3 = dog('shiba inu', 'big', '6 years', 'orange/white')
print(dog1.breed, dog1.size, dog1.age, dog1.color)
print(dog2.breed, dog2.size, dog2.age, dog2.color)
print(dog3.breed, dog3.size, dog3.age, dog3.color)


#4
class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        res = self.num1 + self.num2
        return res
    def sub(self):
        return self.num1 - self.num2
    def mult(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    
num = calculator(2, 5)
print(num.add())
print(num.div())
print(num.sub())
print(num.mult())

#5
class people:
    def __init__(self, gender, age, name):
        self.gender = gender
        self.age = age
        self.name = name

class student(people):
    def __init__(self, gender, age, name, year):
        super().__init__(gender, age, name)
        self.year = year
    def s_intr(self):
        return f"Name's {self.name}, I am in year {self.year}, nice to meet you."
    def s_answer(self):
        return f"Hi, my name is {self.name} and I am in year {self.year}, nice to meet you too."
    def next_lec(self, teach, sub1):
        return f"My next class is with {teach}, {sub1}."

class lecturer(people):
    def __init__(self, gender, age, name, sub): #subject
        super().__init__(gender, age, name)
        self.sub = sub

teach1 = lecturer('male', 32, 'Mike', 'Chemistry')
teach2 = lecturer('female', 30, 'Lilly', 'Biology')
stud1 = student('female', 19, 'Kristi', 2)
stud2 = student('male', 20, 'Noah', 3)
import random
teachs = [teach1, teach2]
rteach1 = random.choice(teachs)
rteach2 = random.choice(teachs)
studs = [stud1, stud2]
rstud1 = random.choice(studs)
def name(stu):
    for i in stu:
        if i != rstud1:
            return i
rstud2 = name(studs)
print(rstud1.s_intr())
print(rstud2.s_answer())
print(stud2.next_lec(rteach1.name, rteach1.sub))
print(stud1.next_lec(rteach2.name, rteach2.sub))

#bonus

class bank:
    def __init__(self, acc_name, balance = 0):
        self.acc_name = acc_name
        self.balance = balance

    def get_na(self):
        return self.acc_name
    def set_na(self, na):
        self.acc_name = na
        return self.acc_name
    def deposit(self, dep):
        self.balance = self.balance + dep
        return f"Transaction is successful, your current balance: {self.balance}."
    def withdraw(self, wit):
        self.balance = self.balance - wit
        return f"Transaction is successful, your current balance: {self.balance}."
    
acc = bank('Sophio')
print(acc.get_na())
print(acc.set_na('Tevdoradze'))
print(acc.deposit(1000))
print(acc.withdraw(300))