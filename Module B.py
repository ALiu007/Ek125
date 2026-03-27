import time
import random

def validation(correctAnswer):
    """Gets user input from the problem presented and returns answer validity and time"""
    answerValid = False
    answerStart = time.time()
    answer = int(input("Your Answer: "))
    answerEnd = time.time()
    answerTime = answerEnd - answerStart

    if answer == correctAnswer:
        if answerTime < 1:
            print("Lightning Fast Answer! Time Bonus awarded (+3)")
        else:
            print("Correct Answer! (+1)")
        answerValid = True
    else:
        print("uh oh that's not right...")

    return answerValid, answerTime


mode = "speed"
if mode == "speed":
    total_time = 0
    while total_time < 20:
        #Example Problem
        print("What is 4*7?")
        validity, answerTime = validation(28)
        total_time += answerTime
        print("Time Elapsed:", round(total_time,3))
    print("Done")