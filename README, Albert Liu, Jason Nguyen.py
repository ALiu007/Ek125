#   Our game is the quick draw math challenge. There are 3 different difficulties (easy, medium, hard), 4 different
# problem types (addition, subtraction, multiplication, division), and 3 different game modes (speed, accuracy,
# streak) to choose from. On the opening menu the player will first be prompted to choose one of the three modes shown.
# Then, after choosing the mode, the player will be prompted to choose one of the four modes shown on screen. Finally,
# before starting the game, the player will be prompted to choose one of three difficulties of problems.
#
#   To get started, we follow a basic scoring system that rewards each player 1 point per correct answer. After each
# question we also give instant feedback on whether the player answered correctly and show a running score. Depending
# on which mode the player chooses, there are various modifiers on scoring.
#
#   For the different problem types, they show questions featuring different math functions. If the player chooses
# addition, then they will get questions featuring addition problems. If the player chooses subtraction, then they will
# get questions featuring subtraction problems. If the player chooses multiplication, then they will get questions
# featuring multiplication problems. If the player chooses division, then they will get questions featuring division
# problems.
#
#   The different difficulties will decide how big the numbers can be in each of the different problem types. For the
# easy difficulty, the numbers that could be used range between 1 and 10. For the medium difficulty, the numbers that
# could be used range between 1 and 50. For the hard difficulty, the numbers that could be used range between 1 and 100.
#
# For the different game modes:
#
#   First, the speed mode. The player gets a 2-minute window where questions will be asked and they can answer. As for
# all the modes, the player is given a time bonus for answering quickly. If the player answers a question in 3 seconds
# or less, they are given an additional 2 points (3 points in total). At the end, the player is shown a menu that says
# that their time is up. It then displays the total points earned, problem solved, accuracy, and average time per
# problem.
#
#   Next, the accuracy mode. The player will get 20 questions to answer. The player is awarded with a base of 1 point
# for each correct answer, and if they answer in 3 or fewer seconds, they will receive 3 points instead. Unlike the
# speed and streak mode, the player will lose a point for each incorrect answer. At the end, the player is shown a
# menu that says that their time is up. It then displays the total points earned, problem solved, accuracy, and average
# time per problem.
#
#   Finally, the streak mode. The player gets a 1-minute window where questions will be asked and they can answer. The
# player is awarded with a base of 1 point for each correct answer, and if they answer in 3 or fewer seconds, they will
# receive 3 points instead. For the streak mode, more correct answers in a row will reward the player with bonus points.
# For example, 2 correct answers in a row gives +1 bonus point, 3 correct answers in a row gives +2 bonus points, 4
# correct answers in a row gives +3 bonus points, etc. However, getting an incorrect answer will reset the streak.
# At the end, the player is shown a menu that says that their time is up. It then displays the total points earned,
# problem solved, accuracy, and average time per problem.