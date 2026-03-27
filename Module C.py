import random
import time

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
    correctAnswer = a+b
    return correctAnswer


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
    correctAnswer = a - b
    return correctAnswer

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
    correctAnswer = a * b
    return correctAnswer

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
    correctAnswer = a/b
    return correctAnswer

def validation(correctAnswer):
    """Gets user input from the problem presented and returns answer validity and time"""
    answerValid = False
    answerStart = time.time()
    answer = int(input("Your Answer: "))
    answerEnd = time.time()
    answerTime = answerEnd - answerStart

    if answer == correctAnswer:
        if answerTime < 3:
            print("Lightning Fast Answer! Time Bonus awarded (+3)")
        else:
            print("Correct Answer! (+1)")
        answerValid = True
    else:
        print("uh oh that's not right...")

    return answerValid, answerTime

print("Modes: (1) Speed, (2) Accuracy, (3) Streak")
modeChoice = input("Choose your mode (1-3): ")
while modeChoice.title() != "1" and modeChoice.title() != "2" and modeChoice.title() != "3":
    print("Invalid Input! Choose a number 1-3.")
    modeChoice = input("Choose your mode (1-3): ")

print("Types of problems: (1) Addition, (2) Subtraction, (3) Multiplication, (4) Division")
typeChoice = input("Choose your type of problem (1-4): ")
while typeChoice.title() != "1" and typeChoice.title() != "2" and typeChoice.title() != "3" and typeChoice.title() != "4":
    print("Invalid Input! Choose a number 1-4.")
    typeChoice = input("Choose your type of problem (1-4): ")

print("Difficulties: Easy, Medium, Hard")
diffChoice = input("Choose your difficulty: ")
while diffChoice.title() != "Easy" and diffChoice.title() != "Medium" and diffChoice.title() != "Hard":
    print("Invalid Input! Choose a difficulty (Easy, Medium, Hard).")
    diffChoice = input("Choose your difficulty: ")

if modeChoice == "1":
    totalTime = 0
    points = 0

    while totalTime < 60:
        if typeChoice.title() == "1":
            correctAnswer = additionProblem()

        elif typeChoice.title() == "2":
            correctAnswer = subtractionProblem()

        elif typeChoice.title() == "3":
            correctAnswer = multiplicationProblem()

        elif typeChoice.title() == "4":
            correctAnswer = divisionProblem()

        validity , answerTime = validation(correctAnswer)
        totalTime += answerTime


        if validity == True:

            if answerTime < 3:
                points += 3
            else:
                points += 1
        print(" ")
        print(f"Elapsed Time: {round(totalTime,2)} seconds")
        print(f"Points: {points}")
        print("")

    print("Time is up!")
    print(f"Total Points Earned: {points}")
