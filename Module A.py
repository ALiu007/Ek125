import random

print("Difficulties: Easy, Medium, Hard")
print("Types of problems: (1) Addition, (2) Subtraction, (3) Multiplication, (4) Division")
diffChoice = input("Choose your difficulty: ")
while diffChoice.title() != "Easy" and diffChoice.title() != "Medium" and diffChoice.title() != "Hard":
    diffChoice = input("Choose your difficulty: ")
typeChoice = input("Choose your type of problem (1-4): ")
while typeChoice.title() != "1" and typeChoice.title() != "2" and typeChoice.title() != "3" and typeChoice.title() != "4":
    typeChoice = input("Choose your type of problem (1-4): ")

def additionProblem ():
    """Selects two random numbers and asks the user for their sum"""
    a = 0
    b = 0
    if diffChoice.title() == "Easy":
        a = random.randint(1,10)
        b = random.randint(1, 10)
    elif diffChoice.title() == "Medium":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
    elif diffChoice.title() == "Hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
    print(f"Addition question: What is {a} + {b}?")
    answerAdd = input("Your answer: ")
    return answerAdd

def subtractionProblem ():
    """Selects two random numbers and asks the user for their difference"""
    a = 0
    b = 0
    if diffChoice.title() == "Easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        while a < b:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
    elif diffChoice.title() == "Medium":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        while a < b:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
    elif diffChoice.title() == "Hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        while a < b:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
    print(f"Subtraction question: What is {a} - {b}")
    answerSub = input("Your answer: ")
    return answerSub

def multiplicationProblem ():
    """Selects two random numbers and asks for their product"""
    a = 0
    b = 0
    if diffChoice.title() == "Easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif diffChoice.title() == "Medium":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
    elif diffChoice.title() == "Hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
    print(f"Multiplication question: What is {a} * {b}")
    answerMult = input("Your answer: ")
    return answerMult

def divisionProblem ():
    """Selects two random numbers and asks for quotient"""
    a = 0
    b = 0
    if diffChoice.title() == "Easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        while a % b != 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
    elif diffChoice.title() == "Medium":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        while a % b != 0:
            a = random.randint(1,50)
            b = random.randint(1, 50)
    elif diffChoice.title() == "Hard":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        while a % b != 0:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
    print(f"Division question: What is {a} / {b}")
    answerDiv = input("Your answer: ")
    return answerDiv


if typeChoice.title() == "1":
    additionProblem()
elif typeChoice.title() == "2":
    subtractionProblem()
elif typeChoice.title() == "3":
    multiplicationProblem()
elif typeChoice.title() == "4":
    divisionProblem()


