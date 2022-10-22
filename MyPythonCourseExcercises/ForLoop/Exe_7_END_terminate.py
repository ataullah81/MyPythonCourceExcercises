#7. Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
#For loop
import sys
name = []
print("Write END to terminate the loop.")
for n in range(sys.maxsize):
    name = str(input("Write your name: "))
    if name != 'END':
        print("Your name is:",name)
    else:
        break
print("I am done.")


"""
# While loop
counter = 0
name = []
print("Write END to terminate the loop.")
while name != 'END':
    name = str(input("Write your name: "))
    if name == 'END':
        print("I am done")
    else:
        counter += 1
        print("Your name is:",name)

"""