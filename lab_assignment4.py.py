#qn1.Function without Parameters:
#ans:
def print_():
    print("Hello, World!")

print_()

output:
Hello, World!

#qn2.Function with Parameter:
#ans:
def add(a,b):
 res = a+b
 print(f"the addition is:{res}")

add(5,7)

output:
the addition is:12 

#qn3.Function with Default Parameter:
#ans:
def greet(name="Aryan verma", greeting="welcome"):
    return f"{greeting}, {name}!"

print(greet())
print(greet("shivam","come"))

output:
welcome, Aryan verma!
come, shivam! 

#qn4.Function with Return Keyword:
#ans:
def mul(a,b):
 res = a*b
 return res

result = mul(5,7)
print(f"the multiplication is:{result}")

output:
the multiplication is:35


#qn5.Recursion:

#a) WAP to print factorial value of a given number using recursion.
#ans:
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

output:
Enter a number: 5
The factorial of this number is: 120

#b) WAP to display Fibonacci series up to 10 iteration using recursion.iteration using recursion.
#ans:
def fib(n, a=0, b=1):
    
    if n <= 0:
        return
    print(a, end=' ')
    fib(n - 1, b, a + b)

num_terms = 10
print(f"Fibonacci series up to {num_terms} iterations:")
fib(num_terms)

output:
Fibonacci series up to 10 
iterations:
0 1 1 2 3 5 8 13 21 34 