def greet():
    print("My name is Ai\n")
def name():
    urname=str(input("What is your name??\n"))
    print("Hello  {0}".format(urname))
    
def greet2():
    ask=str(input("How are you?\n"))
    if ask.lower() == "I m fine" or ask.lower() == "I am fine" or ask.lower() == "fine":
        print("Nice,I'm fine too\n")
    elif "no" in ask:
        print("Its okay we all have bad days, you can do it\n")
    else:
        print("Sorry i don't understand you\n")
def detail():
    country=input("Which country are you from??\n")
    print("Oh nice, i would love to visit {0}, some day soon".format(country))
def question():
    while True:
      que=input("Ask me anything?\n")
      if "countr" in que:
        print("I am from India")
      elif "city" in que:
        print("I am from Bhavnagar")
      elif "age" in que:
        print("I am 21 years old")
      elif "bf" in que:
        print("Sorry, I am alredy taken!!!")
      elif "143" or "love" in que:
        print("Same to you")
      else:
          print("Tata")

    
    
greet()
name()
greet2()
detail()
question()
