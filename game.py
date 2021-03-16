# making a game in python

# this is a quiz game

limit = 1
score = 0

print("Welcome to my game!")
print("Try to answer question correct as many as possible!")

# Asking user to get the name

name = input("Enter your name: ")
if name == "":
    print("You cannot play this game without entering your name!")
else:
    first_question = input("1. Write the name of the owner of Microsoft? ")
    if first_question.lower() == "billgates":
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

    second_question = input("Enter the name of the owner of the facebook? ")
    if second_question.lower() == "mark zuchberg":
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

    third_question = input("Enter the name of the owner of the Amazon? ")
    if third_question.lower() == "jeff bezos":
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

    fourth_question = input("Enter the capital of Pakistan? ")
    if fourth_question.lower() == "islamabad":
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

    fifth_question = input(
        "Enter the name of city which is said that this is the heart of Pakistan? ")
    if fifth_question.lower() == "lahore":
        score += 1
        print("Correct answer")
    else:
        print("Wrong answer")

    if score > limit:
        print(f"You have answered {score} questions correctly.")
    else:
        print(f"You have answered {score} question correctly.")

    print(f"Your final score is {score}")


# Asking user to tell us how's this program works...

    rating = input(
        "How's this program works. If you want to tell us. Write [Y/N]")

    if rating.lower() == "yes" or rating.lower() == "y":
        opinion = input("Enter your opinion? ")

    # Writing the user's opinion in the file...

        file = open("index.txt", "a")

        file.write(
            f"\n -------- \nName: {name} \nScore: {score} \nOpinion: {opinion}")

        file.close()

        print("Thanks!")
    elif rating.lower() == 'no' or rating.lower() == 'n':
        print("No matter!")
    else:
        print("Invalid answer!")
