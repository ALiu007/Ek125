import random

#Inputs for difficulty and types of problem
print("Difficulties: Easy, Medium, Hard")
print("Types of problems: (1) Addition, (2) Subtraction, (3) Multiplication, (4) Division")
diffChoice = input("Choose your difficulty: ")
while diffChoice.title() != "Easy" and diffChoice.title() != "Medium" and diffChoice.title() != "Hard":
    diffChoice = input("Choose your difficulty: ")
typeChoice = input("Choose your type of problem (1-4): ")
while typeChoice.title() != "1" and typeChoice.title() != "2" and typeChoice.title() != "3" and typeChoice.title() != "4":
    typeChoice = input("Choose your type of problem (1-4): ")

def additionProblem():
    """Selects two random numbers and asks the user for their sum"""
    a = 0
    b = 0
    if diffChoice.title() == "1":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 10
    elif diffChoice.title() == "2":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        # if the difficulty choice is medium, generates 2 random integers between 1 and 50
    elif diffChoice.title() == "3":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 100
    print(f"Addition question: What is {a} + {b}?")
    correctAnswer = a + b
    # sets the correct answer as the correct answers as the two integers added together
    return correctAnswer


def subtractionProblem():
    """Selects two random numbers and asks the user for their difference"""
    a = 0
    b = 0
    if diffChoice.title() == "1":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 10
        while a < b:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            # if the random integers subtract to a negative number, regenerates the integers
    elif diffChoice.title() == "2":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        # if the difficulty choice is medium, generates 2 random integers between 1 and 50
        while a < b:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
    elif diffChoice.title() == "3":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 100
        while a < b:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
    print(f"Subtraction question: What is {a} - {b}")
    correctAnswer = a - b
    # sets the correct answer as the two integers subtracted with each other
    return correctAnswer


def multiplicationProblem():
    """Selects two random numbers and asks for their product"""
    a = 0
    b = 0
    if diffChoice.title() == "1":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 10
    elif diffChoice.title() == "2":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        # if the difficulty choice is medium, generates 2 random integers between 1 and 50
    elif diffChoice.title() == "3":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 100
    print(f"Multiplication question: What is {a} * {b}")
    correctAnswer = a * b
    # sets the correct answer as the two integers multiplied together
    return correctAnswer


def divisionProblem():
    """Selects two random numbers and asks for quotient"""
    a = 0
    b = 0
    if diffChoice.title() == "1":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        # if the difficulty choice is easy, generates 2 random integers between 1 and 10
        while a % b != 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            # if the division doesn't result in a whole number, it regenerates the integers
    elif diffChoice.title() == "2":
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        # if the difficulty choice is medium, generates 2 random integers between 1 and 50
        while a % b != 0:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
    elif diffChoice.title() == "3":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        # if the difficulty choice is hard, generates 2 random integers between 1 and 100
        while a % b != 0:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
    print(f"Division question: What is {a} / {b}")
    correctAnswer = a / b
    # sets the correct answer as the two integers divided by each other
    return correctAnswer


if typeChoice.title() == "1":
    additionProblem()
elif typeChoice.title() == "2":
    subtractionProblem()
elif typeChoice.title() == "3":
    multiplicationProblem()
elif typeChoice.title() == "4":
    divisionProblem()

