
#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.
HIGH_SCORE = 95
 
# Get the test scores.
#because the input() function returns a string (text), and you're trying to perform mathematical operations (+ and /) on strings. You need to convert the input values to numbers first
try:  
  test1 = float(input('Enter the score for test 1: '))
  test2 = float(input('Enter the score for test 2: '))
  #third test score
  test3 = float(input('Enter the score for test 3: '))
  # Calculate the average test score.
  #add parentheses 
  average = (test1 + test2 + test3) / 3
  # Print the average.
  print('The average score is', average)
# If the average is a high score,
# congratulate the user.
#correct the HIGH_SCORE variable name 
  if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!') #this line should only print if the average is greater or equal to HIGH_SCORE
except ValueError:
    print('Error: Please enter numeric values for all test scores.')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width 
#of two rectangles and prints to the user the area of both rectangles. 
try:
  length_1 = float(input('Enter the length for first rectangle: '))
  width_1 = float(input('Enter the width for first rectangle: '))

  area_1 = length_1 * width_1
  print('The area for first rectangle is', area_1)
except ValueError:
    print('Error: The length and width can only be a number. Please run the program again.')
    
#To handle non-numeric input and provide a user-friendly error message, you can use a try-except block
try:
    length_2 = float(input('Enter the length for second rectangle: '))
    width_2 = float(input('Enter the width for second rectangle: '))
    area_2 = length_2 * width_2
    print('The area for second rectangle is', area_2)
except ValueError:
    print('Error: The length and width can only be a number. Please run the program again.')

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
try:
  name= input('Enter your name: ')
  age = float(input('Enter your age: '))
#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today

# Convert age to string for concatenation
  print('Happy birthday, ' + name + '! You are ' + str(age) + ' years old today')
except ValueError:
    print('Error: The age can only be a number. Please run the program again.')
