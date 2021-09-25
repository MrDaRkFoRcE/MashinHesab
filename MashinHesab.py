#Programmer : MrDaRkFoRcE
#Telegram : @ThE_DaRkFoRcE

while True:
    number1 = int(input("enter you number : ".title()))
    vasat = input("select the type ( + , - , * , / ) : ".title())
    number2 = int(input("enter you number : ".title()))

    if vasat == "+":
        print(number1, "+", number2, "=", number1+number2)
    elif vasat == "-":
        print(number1, "-", number2, "=", number1-number2)
    elif vasat == "*":
        print(number1, "*", number2, "=", number1*number2)
    elif vasat == "/":
        print(number1, "/", number2, "=", number1/number2)
    elif vasat == "//":
        print(number1, "//", number2, "=", number1//number2)
    elif vasat == "**":
        print(number1, "**", number2, "=", number1**number2)
    elif vasat == "%":
        print(number1, "%", number2, "=", number1%number2)
    elif vasat == "^":
        print(number1, "^", number2, "=", number1^number2)
    else :
        print("Vorodi Namotabar Ast !")