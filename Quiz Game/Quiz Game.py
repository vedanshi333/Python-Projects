print("Quiz game")
choice=input("Do you want to play it? ")
print("Type skip to skip the questions as it has negative marking")
if choice.lower() == "yes":
    print("Let's play it ")
elif choice.lower() =="no":
    print("Okay bye")
    quit()
else:
    print("You can only use Yes or no")
    quit()
count=0
que1=str(input("How many colours are there in a rainbow?"))
if que1.lower() == "7" or que1.lower()=="seven":
    print("Correct answer ")
    count=count+10
elif que1.lower()=="skip":
    print("You skipped it")
else:
    print ("Wrong answer ")
    count=count-5
que1=str(input("How many days are rhere in a leap year?"))
if que1.lower() == "366" or que1.lower()=="three hundred sixty six":
    print("Correct answer")
    count=count+10
elif que1.lower()=="skip":
    print("You skipped it")
else:
    print ("Wrong answer ")
    count=count-5
que1=str(input("What is full form of idk"))
if que1.lower() ==" i do not know" or que1.lower()=="i don't know":
    print("Correct answer ")
    count=count+10
elif que1.lower()=="skip":
    print("You skipped it")
else:
    print ("Wrong answer ")
    count=count-5
print("Your score is {}:".format(count))
