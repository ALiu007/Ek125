# Contributions:
#
# Albert: I Worked on module A. I Created the functions in order to present problems depending on different difficulties
# (easy, medium, hard) and different math functions (addition, subtraction, multiplication, division). I Created the main
# menu that prompts the user for which difficulty, question type, and game mode the player wants to play. I attempted
# to create the accuracy mode for module C, and, with Jason, was able to debug an issue that was breaking the code for
# the speed mode. I create the README with instructions to open the game on pyCharm and how to play it with rules.
#
# Jason: I worked on Module B and incorporated the validation function which asks for user input and checks if it is
# correct. It then returns the answer time and if the answer was correct to variables that are used in the points
# process as well as game stats. I also did the time part in Module B which gets the answer times and total time using
# the time module in python. I also partly worked on Module C and made the streak and speed modes for the game. I also
# tidied up the interface in the integration part so everything flowed and looked good.
#
# Known issues and limitations:
#
# Originally, if the player just pressed enter and put nothing as an answer, it would stop the code and crash the game.
# However, we added a while loop to check if the answer entered wasn't an integer, and if it wasn't, it would reprompt
# the player and add that they should enter an integer.
#
# A limitation we had was a complexity of the questions that we could ask. In a game such as this, there has to be some
# sort of standardization in what players can answer and the types of questions we can ask. For example, dividing by
# non-whole numbers would create issues where the player may not intuitively know how many decimal places to put.
# For a speed mode like the one we have, we want the player to simply be able to answer as quick as they can rather than
# have to think about negatives and many decimals.
#
# Another limitation is the amount of customizability just using python allows us. We can only go so far making menus
# look so good using stars and equal signs. We would have loved to have a better looking integration, but we are limited
# in the tools that we can use to do so.
#
# Future enhancement ideas:
#
# A big enhancement would be adding more colors or symbols to make the menus and integration look better and more
# pleasing rather than simple equals, stars, and the words we need to have. Making the ability to have a better looking
# UI would make it look better and improve player experience.
#
# Another future enhancement would be adding more modes and more types of math problems that we could do. A big thing
# that we couldn't do this time was mixing all the math types together, so having a mode to do that would be great.
# Having different math types could also vary the difficulty depending on what level of math a player chooses such as
# doing integrals and derivatives versus just addition and subtraction.