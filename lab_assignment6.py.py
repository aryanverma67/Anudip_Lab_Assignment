#Q1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

#Ans:def readData():
    fileName = input("enter your file with extension: ")
    fopen = open(fileName,"r")
    data  =fopen.read().split()
    for i in data:
        print(i,end=" ")
        fopen.close()
readData()


#output: 
enter your file with extension: sample.txt
hy this side aryan can u tell me how i help u!


#Q2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

#Ans:def countwords():
    fileName = input("enter your file with extension: \n")
    fopen = open(fileName,"r")
    data  =fopen.read().split()
    count = 0
    for i in data:
        print(i,end=" ")
        count+=1
    print(f"the total no of words is: {count}\n")
    fopen.close()
countwords()


#output: 
 enter your file with extension: sample.txt
hy this side aryan can u tell me how i help u! 
the total no of words is: 12


#Q3. Write a function in Python to count uppercase character in a text file “ABC.txt”

#Ans:
def checkuppercase():
    fileName = input("enter your file with extension: \n")
    fopen = open(fileName,"r")
    data  =fopen.read()
    count = 0
    for i in data:
        print(i,end=" ")
        if i.isupper():
            count+=1
    print(f"the total no of uppercase char is: {count}\n")
    fopen.close()
checkuppercase()


#output: 
enter your file with extension: 
abc.txt
H y   T h i s   S i d e   A 
r y a n   C a n   T e l l   
M e   H o w   i   H e l p   
u ! the total no of uppercase char is: 9



#Q4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.


#Ans:
def displayWords():
    fileName = input("enter your file with extension: \n")
    fopen = open(fileName,"r")
    data  =fopen.read().split()
    for i in data:
        if len(i)<4:
            print(i)
    fopen.close()
displayWords()

#output: 
enter your file with extension:
sample.txt 
hy
can
u
me
how
i
u!
