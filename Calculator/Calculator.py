import math

# Function to perform addition of two numbers
def add(number1, number2):
    return (number1 + number2)

# Function to perform subtraction of two numbers
def subtract(number1, number2):
    return (number1 - number2)

# Function to perform multiplication of two numbers
def multiply(number1, number2):
    return (number1 * number2)

# Function to perform division of two numbers

def divide(number1, number2):
    return (number1 / number2)

def rootof(a):
    print(a**0.5)

def trigo(deg):
    if trigochoose.lower() == "sinof":
        x = math.sin(math.radians(deg))
    elif trigochoose.lower() == "cosof":
        x = math.cos(math.radians(deg))
    elif trigochoose.lower() == "tanof":
        x = math.tan(math.radians(deg))
    elif trigochoose.lower() == "cosecof":
        x = math.cosec(math.radians(deg))
    elif trigochoose.lower() == "secof":
        x = math.sec(math.radians(deg))
    print(x)

print("Operation Menu -\n"
      "1. Addition of two numbers\n"
      "2. Subtraction of two numbers\n"
      "3. Multiplication of two numbers\n"
      "4. Division of two numbers\n"
      "5. square root  \n"
      "6  Trigonometry\n"
      "7. Logarithm :")

# Taking input from the user
select = int(input("Select operations form 1, 2, 3, 4 5 6 7 8:\n"))

if select == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "+", num2, "=" , add(num1, num2))

elif select == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "-", num2, "=",subtract(num1, num2))

elif select == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "*", num2, "=",multiply(num1, num2))

elif select == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "/", num2, "=",divide(num1, num2))

elif select == 5:
    choose = str(input("Enter which opeartion you want tp perform(square root \n)"))
    x = int(input("Enter the number"))
    y = rootof(x)
    
elif select == 6:
    trigochoose = input("Choose the function you want to perform \nsinof(sin) \n cosof(cos)\n tanof(tan)\n secof(sec)\n cosecof(cosec)\n cotof(cot) \n:")
    deg = float(input("Choose degrees"))
    m = trigo(deg)
elif select == 7:
    a = int(input("Enter a number whose value you want to "))
    base = int(input("Enter the base"))
    print(math.log(a, base))

else:
    print("Invalid input!")
