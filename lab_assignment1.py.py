#Q.1 print helloworld

#ans 
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("hello world")
print("hello world")

output:
hello world



#Q.2 describe local variable and global variable code

#ans:
global_variable = 40

def var_func():
    local_variable = 10
    print(f"Inside the function, local_variable: {local_variable}")

var_func() #its call local variable and print the statement

# print(local_variable) 
# it cause an error because local scope


print(global_variable)
# its run perfectly because global scope

output:
Inside the function, local_variable: 10
40


#Q.3 Write a code that describe Indentation error

#ans:
 indentation error  code
def my_function():
 print("This will cause an indentation error")

my_function()

output:
indentation error



#Q.4 write a code that describe local and global variable with same name
#ans:
# same name  local and global variable code 
# Global variable
variable = "I am a global variable"

def var_func():
    # Local variable with the same name as the global variable
    variable = "I am a local variable"
    print(f"Inside the function: {variable}")


# Calling the function
var_func()

# Accessing the global variable outside the function
print(f"Outside the function: {variable}")

output:
Inside the function: I am a local variable
Outside the function: I am a global variable


#Q.5 Write a code for string, int and float input.
#ans:
integer = int(input("enter your number: "))
float = float(input("enter float number: "))
string = input("enter a name: ")


print(f"the integer value is : {integer}")
print(f"the flaot value is : {float}")
print(f"the name  is : {string}")


print("the integer value is :",integer)
print("the flaot value is : ",float)
print("the name  is :" ,string)

output:
enter your number: 56
enter float number: 76
enter a name: 89
the integer value is : 56
the flaot value is : 76.0       
the name  is : 89
the integer value is : 56       
the flaot value is :  76.0      
the name  is : 89





