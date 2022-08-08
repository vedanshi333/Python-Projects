def greet():
    print("My name is Ai")
def name():
    urname=str(input("What is your name??\n"))
    print("Hello {0}".format(urname))
def greet2():
    ask=str(input("How are you?\n"))
    if "not" not in ask:
        print("Nice,I'm fine too\n")
    elif "not" in ask:
        print("Its okay we all have bad days, you can do it\n")
    else:
        print("Sorry i don't understand you\n")
def detail():
    country=input("Which country are you from??\n")
    print("Oh nice, i would love to visit {0}, some day soon".format(country))
def ques():
    while True:
        que=input("Ask me any questions \n")
        if "city" in que:
            print("I am from Bhavnagar \n")
        if "food" in que:
            print("I eat healthy food, but i love Pizza its my fav food\n")
        if "hobbies" in que:
            print("My hobbies are cooking, listening to songs and watching dramas\n")
        if "friends" in que:
            print("Vishnu is my bestfriend \n")
        if "study" in que:
            print("I m studying EC Engineering from LDCE\n")
        if "bye" in que:
            break
        
greet()
name()
greet2()
detail()
ques()
print("It was nice to talk to you, see you soon, Good bye :)\n")
