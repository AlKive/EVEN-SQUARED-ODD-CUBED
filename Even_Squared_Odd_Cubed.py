# BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 4
#This program reads a text file that contains a set of numbers. 
# Then, the even and odd numbers will be obtained from the text file. 
# The extracted even numbers will be squared and the odd numbers will be cubed. 
# The result will be transferred to separate files.

#import the necessary module
from pyfiglet import figlet_format
import pygame
from termcolor import colored
import pyfiglet
from colorama import Back, Fore, Style, init
import time


# OPEN file (numbers.txt, "w") as Number_File
with open("number.txt", 'w') as Number_File:
  #loop the user input function  
  while True :
     try:
        #PROMPT the user
         print(Fore.RED + "Enter any key to stop input: ")
        # GET user input (numbers/Integers) and store it in numbers.txt file
         user = int(input(Fore.LIGHTBLUE_EX + "Enter a number: " + Fore.YELLOW))
         if user <= 0 or user >= 0:
           #APPEND the integer inputs into the number.txt file
           Number_File.write(str(user) + "\n")
           continue
     except:
         break      
with open("number.txt", 'r') as Number_File, open("even.squared.txt", 'w') as Even_Squared, open("odd.cubed.txt", 'w') as Odd_Cubed:
        # LOOP the lines in number.txt file
         for line in Number_File:
        # ASSIGN each line from number.txt as an integer variable
          Number = int(line)
        # CHECK if Number is EVEN
          if Number % 2 == 0:
            #SQUARE the even number
            New_Even = Number ** 2
            # APPEND the new number to even.squared.txt file
            Even_Squared.write(str(New_Even) + "\n")

        # CHECK if Number is ODD
          elif Number % 2 != 0:
            #CUBE the odd number
            New_Odd = Number ** 3
            # APPEND the new number to odd.txt file
            Odd_Cubed.write(str(New_Odd) + "\n")

print("Processing...")
time.sleep(2)

#DISPLAY the numbers in even.squared.txt
with open("even.squared.txt", 'r') as Even_Squared :    
  even = Even_Squared.read().split('\n')
  text = "EVEN Squared : "
font = "digital"
color = "yellow"
output = pyfiglet.figlet_format(text, font=font, width=200)
outputColor = colored(output, color)

time.sleep(2)
print(Fore.YELLOW + "=" * 100)
time.sleep(2)
print(Fore.LIGHTCYAN_EX + "╔═*.·:·.✧ ✦ ✧.·:·.*═╗" * 5)
for line in outputColor.split("\n"):
    print(line.center(80))
print(Fore.LIGHTCYAN_EX + "╚═*.·:·.✧ ✦ ✧.·:·.*═╝" *5 )  
time.sleep(3)
print(Fore.LIGHTWHITE_EX + line.center(20) + str(even))



#DISPLAY the numbers in odd.cubed.txt
with open("odd.cubed.txt", 'r') as Odd_Cubed:  
  odd = Odd_Cubed.read().split('\n')  
  text = " ODD Cubed : "
font = "digital"
color = "yellow"
output = pyfiglet.figlet_format(text, font=font, width=200)
outputColor = colored(output, color)

time.sleep(2)
print(Fore.YELLOW + "=" * 100)
time.sleep(2)
print(Fore.LIGHTCYAN_EX + "┏━━━✦❘༻༺❘✦━━━┓" * 7)
for line in outputColor.split("\n"):
    print(line.center(80))
print(Fore.LIGHTCYAN_EX + "┗━━━✦❘༻༺❘✦━━━┛" * 7) 
time.sleep(3) 
print(Fore.LIGHTWHITE_EX + line.center(20) + str(odd))


