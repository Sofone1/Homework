# hello name-is gamotana:
name = input('your name: ')
print('Hello', name)

# ricxvi martivia tu shedgenili:
number = int(input("Enter any Number : "))
count = 0
for i in range(2, number):
    if number % i == 0:
        count += 1
if count >= 1:
    print(number, "is a Composite Number")
else:
    print(number, "is a Prime Number")

# rock, paper, scissors:
import random
while True:
    user = input("choose - rock, paper or scissors: ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)
    print('You chose', user, '-', 'computer chose', computer)

    if user == computer:
        print('Both players selected', user, '-' " It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock breaks scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    break

# calculator:
number1 = int(input('enter any number: '))
operation = str(input('enter an oparation (+, -, *, /, ^): '))
number2 = int(input('enter any number: '))
if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
elif operation == '^':
    print(number1 ** number2)
