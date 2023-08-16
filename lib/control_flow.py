#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" and password == "12345"):
        print("Access Granted")
    elif (username == "ADMIN" and password == "12345"):
        print("Access Granted")
    else:
        print("Access denied")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        print("It's brisk out there!")
    elif (temperature >= 40 and temperature <= 65):
        print("It's a little chilly out there!")
    elif (temperature > 85):
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")

def fizzbuzz(num):
    # your code here
    if (num%3 == 0 and num%5 == 0):
        print("fizzbuzz")
    elif num%3 == 0:
        print("fizz")
    elif num%5 == 0:
        print("buzz")
    else:
        print (num)

def calculator(operation, num1, num2):
    
    if operation == "+" :
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    elif operation == "/":
        result = num1 / num2
        print(result)
    else:
        print("Invalid Operation")
        return "None"

    

admin_login("admin","12345")
hows_the_weather(60)
fizzbuzz(45)
calculator("*", 3, 2)
