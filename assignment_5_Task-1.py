'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

dict = {'Alice':85, 'Ram':99, 'Krishna':100, 'Shiva':100, 'Ravan':35}

name = input("Enter the student's name: ").capitalize()
# print(dict['john'])
try:
    print("{}'s marks: ".format(name),dict[name])
except KeyError:
    print("Student not found.")