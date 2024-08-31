#1. Write a Python program to Count all letters, digits, and special symbols from the given string

 Input = “P@#yn26at^&i5ve” 

#Ans:
sentence = input("enter your sentence: ")
n = len(sentence)
char = 0
digit =0
space = 0
symbol = 0
for i in range(0,n):
    if sentence[i].isalpha():
        char+=1
    elif sentence[i].isdigit():
        digit +=1
    elif sentence[i].isspace():
         space+=1
    else:
        symbol +=1
print(f"total character is :{char}\n total digits is: {digit}\n total spaces is: {space}\n total symbols is:{symbol}\n")

#Output: 
enter your sentence: P@#yn26at^&i5ve
total character is :8
 total digits is: 3  
 total spaces is: 0  
 total symbols is:4 


2. Write a Python program to remove duplicate characters of a given string.

 Input = “String and String Function” 

#Ans:
sentence = input("enter your sentence: ")
n = len(sentence)
word = sentence.upper()
newWord = "" 

for i in range(0,n):
    char = sentence[i]  
    if char not in newWord:
        newWord+=char

print(f"after removing duplicates :{newWord}")

#output:  
enter your sentence: String and String Function   
total vowels is: 3
enter your sentence: String and String Function   
after removing duplicates :STRING ADFUCO


#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

#Ans:
sentence = input("enter your sentence: ")
n = len(sentence)
upper = 0
lower = 0
digit =0
symbol = 0
for i in range(0,n):
    if sentence[i].isupper():
        upper+=1
    elif sentence[i].islower():
        lower+=1
    elif sentence[i].isdigit():
        digit =+1
    else:
        symbol +=1
print(f"total uppercase is :{upper}\n total lowercase is:{lower}\n total digits is: {digit}\n  total symbols is:{symbol}\n")


#Output:
enter your sentence: Hell0 W0rld ! 123 * # welcome to pYtHoN
total uppercase is :5
 total lowercase is:18   
 total digits is: 5      
 total symbols is:11    


4. Write a Python Count vowels in a string 

input= “Welcome to Python Assignment” 

#Ans:
sentence = input("enter your sentence: ")
n = len(sentence)
vowels ="aeiou"
vowel = 0
word = sentence.upper()

for i in range(0,n):
    if word[i] == "A" or word[i] == "E" or word[i] == "E" or word[i] == "O" or word[i] == "U":
        vowel+=1

print(f"total vowels is: {vowel}")


#output:
enter your sentence: Welcome to Python Assignment 
total vowels is: 7        
