
#1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
#ans:
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 10)

def check_no(num):
    speak("are yu ready to see the result")

    if num%2==0:
        speak(f" {num} is a even number")
        print( f" {num} is a even number")
    else:
        speak(f" {num} ia a odd number")
        print( f" {num} ia a odd number"
)
speak("enter your number for yu check odd and even ")   
number = int(input("enter your number:"))

check_no(number)
    
output:
enter your number:7
7 ia a odd number



#2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
#ans
# 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)


speak("enter your age: ")
person_age = int(input("enter your Age: "))

speak("are yu ready to see the result")

if(person_age>18):
     speak("yu are eligible to vote")
     print("you are  eligible to vote")
elif person_age == 18:
     speak("congratulations on your first vote")
     print("congratulations on your first vote")
else:
     speak("yu are not eligible to vote")
     print("you are not elgible to vote")

output:
enter your Age: 22
you are  eligible to vote

enter your Age: 4
you are not elgible to vote

#3.Write a Python program that determines if a given year is a leap year or not.
#ans:
def check_leap(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

year = int(input("Enter a year: "))
if check_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

def table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")



output:
Enter a year: 2024
2024 is a leap year.

#4.Create a Python program that checks if a user-given number is positive, negative, or zero.
#ans:


def check_posNeg(num):
    if num>0:
        print(f"{num} is a positive number")
    elif num == 0:
        print(f"number is zero ")
    else:
        print(f"{num} is a negative number")

num = int(input("enter your number: "))
check_posNeg(num)

output:
enter your number: 5
5 is a positive number

#5.Write a Python program that determines the largest of three numbers entered by the user.
#ans:
def greatest(a, b, c):
    if a == b == c:
        print("All three numbers are equal.")
    elif a == b:
        if a > c:
            print(f"{a} and {b} are equal and greater than {c}.")
        else:
            print(f"The greatest number is {c}, but other numbers are equal.")
    elif a == c:
        if a > b:
            print(f"{a} and {c} are equal and greater than {b}.")
        else:
            print(f"The greatest number is {b}, but other numbers are equal.")
    elif b == c:
        if b > a:
            print(f" b and c  are equal and greater than {a}.")
        else:
            print(f"The greatest number is {a}, but other numbers are equal.")
    else:
        if a > b and a > c:
            print(f"The greatest number is {a}.")
        elif b > a and b > c:
            print(f"The greatest number is {b}.")
        else:
            print(f"The greatest number is {c}.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

greatest(a, b, c)

output:
Enter the first number: 78
Enter the second number: 78
Enter the third number: 90
The greatest number is 90, but other numbers are equal.

