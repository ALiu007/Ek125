import time

#Function to check answer
def validation(correctAnswer):
    """Gets user input from the problem presented and returns answer validity and time"""
    answerValid = False
    #Getting the time at the start of the input
    answerStart = time.time()
    #Getting user input for their answer
    answer = input("Your Answer: ")
    #Confirming input is a int
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
