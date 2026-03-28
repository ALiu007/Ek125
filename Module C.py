'''
We both worked on Module C, and we combined Module A and Module B together
so Module C would be easier to work on. This is also the final version of
our code
'''

import random
import time


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

# Tested module A 5 times, and everything worked as planned

def validation(correctAnswer):
    """Gets user input from the problem presented and returns answer validity and time"""
    answerValid = False
    #Getting the time at the start of the input
    answerStart = time.time()
    #Getting user input for their answer
    answer = input("Your Answer: ")
    #Confirming input is an int
    while answer.isnumeric() == False:
        print("Please Enter a Integer")
        answer = input("Your Answer: ")

    #Getting time at the end of the input and then subtracting the end from the start to get the seconds it took
    answerEnd = time.time()
    answerTime = answerEnd - answerStart

    #Checks if the input answer equals the correct answer and then prints the points gained
    if int(answer) == correctAnswer:
        if answerTime < 2:
            print("Lightning Fast Answer! Time Bonus awarded (+3)")
        else:
            print("Correct Answer! (+1)")
        answerValid = True
    else:
        print("uh oh that's not right...")

    #Returns answer validity as well as the answer time for statistics and point distribution
    return answerValid, answerTime

# Tested module B 5 times, and everything worked as planned

#Main Function Starts
print("="*40)
print("Welcome to the Quick-Draw Math Challenge")
print("="*40)
print("Answer as many math problems as correct as possible. \nProblems increase in difficulty, and the game tracks accuracy and speed.")
print("")
print("Modes: \n(1) Speed - In 2 minutes, try to answer the most problems possible \n(2) Accuracy - Answer 20 problems with no time limit, wrong answers are penalized \n(3) Streak - In 1 minute, answer as many questions as possible with a chain bonus for consecutive correct answers")

modeChoice = input("Choose your mode (1-3): ")
while modeChoice.title() != "1" and modeChoice.title() != "2" and modeChoice.title() != "3":
    print("Invalid Input! Choose a number 1-3.")
    modeChoice = input("Choose your mode (1-3): ")

print("")
print("Types of problems: \n(1) Addition \n(2) Subtraction \n(3) Multiplication \n(4) Division")
typeChoice = input("Choose your type of problem (1-4): ")
while typeChoice.title() != "1" and typeChoice.title() != "2" and typeChoice.title() != "3" and typeChoice.title() != "4":
    print("Invalid Input! Choose a number 1-4.")
    typeChoice = input("Choose your type of problem (1-4): ")

print("")
print("Difficulties \n(1) Easy - Problem use numbers 1-10 \n(2) Medium - Problem use numbers 1-50 \n(3) Hard - Problem use numbers 1-100")
diffChoice = input("Choose your difficulty: ")
while diffChoice.title() != "1" and diffChoice.title() != "2" and diffChoice.title() != "3":
    print("Invalid Input! Choose a difficulty (Easy, Medium, Hard).")
    diffChoice = input("Choose your difficulty: ")
print("")

if modeChoice == "1":
    totalTime = 0
    points = 0
    totalProblems = 0
    correctProblems = 0

    while totalTime < 120:
    # Ass long as total time is less than 120 seconds (2 minutes), the game will keep going
        if typeChoice.title() == "1":
            correctAnswer = additionProblem()
            # If addition is chosen, calls the additionProblem function and sets the correct answer as that

        elif typeChoice.title() == "2":
            correctAnswer = subtractionProblem()
            # If subtraction is chosen, calls the subtractionProblem function and sets the correct answer as that

        elif typeChoice.title() == "3":
            correctAnswer = multiplicationProblem()
            # If multiplication is chosen, calls the multiplicationProblem function and sets the correct answer as that

        elif typeChoice.title() == "4":
            correctAnswer = divisionProblem()
            # If division is chosen, calls the divisionProblem function and sets the correct answer as that

        validity, answerTime = validation(correctAnswer)
        totalTime += answerTime

        totalProblems += 1

        if validity == True:
            correctProblems += 1
            if answerTime < 3:
                points += 3
            else:
                points += 1
        # if validity is true, adds a point for correctness, and if answered within 3 seconds, adds 3 points

        print(" ")
        print("=" * 40)
        print("=== Game Status ===")
        print(f"Elapsed Time: {round(totalTime, 2)} seconds")
        print(f"Points so far: {points}")
        print("="*40)
        print("")
    print("="*40)
    print("Time is up!")

if modeChoice == "2":
    totalTime = 0
    points = 0
    totalProblems = 0
    correctProblems = 0

    for i in range(1,21):
        if typeChoice.title() == "1":
            correctAnswer = additionProblem()
            # If addition is chosen, calls the additionProblem function and sets the correct answer as that

        elif typeChoice.title() == "2":
            correctAnswer = subtractionProblem()
            # If subtraction is chosen, calls the subtractionProblem function and sets the correct answer as that

        elif typeChoice.title() == "3":
            correctAnswer = multiplicationProblem()
            # If multiplication is chosen, calls the multiplicationProblem function and sets the correct answer as that

        elif typeChoice.title() == "4":
            correctAnswer = divisionProblem()
            # If division is chosen, calls the divisionProblem function and sets the correct answer as that

        validity, answerTime = validation(correctAnswer)

        totalTime += answerTime
        totalProblems += 1

        if validity == True:
            correctProblems += 1
            if answerTime < 3:
                points += 3
            else:
                points += 1
            # if validity is true, adds a point for correctness, and if answered within 3 seconds, adds 3 points
        elif validity == False:
            print("Wrong Answer (-1)")
            points -= 1
            # if validity is false, subtracts a point from the points count

        print("")
        print("=" * 40)
        print("=== Game Status ===")
        print(f"Question {i}/20 completed")
        print(f"Points so far: {points}")
        print("=" * 40)
        print("")

if modeChoice == "3":
    totalTime = 0
    points = 0
    totalProblems = 0
    correctProblems = 0
    previousProblemCorrect = False
    c = 0

    while totalTime < 60:
        if typeChoice.title() == "1":
            correctAnswer = additionProblem()
            # If addition is chosen, calls the additionProblem function and sets the correct answer as that

        elif typeChoice.title() == "2":
            correctAnswer = subtractionProblem()
            # If subtraction is chosen, calls the subtractionProblem function and sets the correct answer as that

        elif typeChoice.title() == "3":
            correctAnswer = multiplicationProblem()
            # If multiplication is chosen, calls the multiplicationProblem function and sets the correct answer as that

        elif typeChoice.title() == "4":
            correctAnswer = divisionProblem()
            # If division is chosen, calls the divisionProblem function and sets the correct answer as that

        validity, answerTime = validation(correctAnswer)
        totalTime += answerTime

        totalProblems += 1

        if validity == True:
            if previousProblemCorrect == True:
                c += 1
                print(f"Chain Bonus (+{c})")
                points += c
            correctProblems += 1

            if answerTime < 3:
                points += 3
            else:
                points += 1
            # if validity is true, adds a point for correctness, and if answered within 3 seconds, adds 3 points
            previousProblemCorrect = True

        elif validity == False:
            previousProblemCorrect = False
            c = 0
        # if validity is false, resets the chain count back to 0


        print(" ")
        print("=" * 40)
        print("=== Game Status ===")
        print(f"Elapsed Time: {round(totalTime, 2)} seconds")
        print(f"Points so far: {points}")
        print("=" * 40)
        print("")

    print("="*40)
    print("Time is up!")

#Printing end game statistics
print("="*40)
print("*** End Game Statistics ***")
print("=" * 40)
print(f"Total Points Earned: {points}")
print(f"Problems Solved: {correctProblems}")
print(f"Accuracy: {round((correctProblems/totalProblems)*100,2)}%")
print(f"Average Time Per Problem: {round(totalProblems/totalTime,2)} seconds")

# Tested module C 5 times, and everything worked as planned
# Tested the main code 5 times, and everything worked as planned
