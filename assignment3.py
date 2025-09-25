'''
Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. 
Then using if statements and else statements print the user a message recommending a meal. 
For example, 
the meal was breakfast, you could say something like, “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast, 
lunch, or dinner.
'''
# Program: Meal Recommendation
meal = input("What meal would you like to have: breakfast, lunch, or dinner? ").lower()

if meal == "breakfast":
    print("How about some bacon and eggs?")
elif meal == "lunch":
    print("How about a fresh salad for lunch?")
elif meal == "dinner":
    print("How about grilled chicken for dinner?")
else:
    print("Please enter either breakfast, lunch, or dinner.")
'''
Q2: The mailroom has asked you to design a simple payroll program that calculates a student 
employee’s gross pay, including any overtime wages. If any employee works over 20 hours in 
a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
You should take in the user’s input for the number of hours worked, and their rate of pay.
'''
try:
  hours_worked = float(input('Please enter number of hours worked :'))
  pay_rate = float(input('Please enter your pay rate :'))
except ValueError:
    print("Oops! That wasn't a valid input. Please enter correct numbers.")

# Calculate pay
if hours_worked > 20:
  over_time = hours_worked - 20
  pay = (20 * pay_rate) + (over_time * pay_rate * 1.5)
  print(f"Your gross pay is: {pay}")
else:
  pay = hours_worked * pay_rate
  print(f"Your gross pay is: {pay}")

'''
Q3: Write a function named times_ten. The function should accept an argument and display 
the product of its argument multiplied times 10.
'''

def times_ten(num):
  return num*10
try:
  number = int(input('Please enter a number: '))
  result = times_ten(number)
  print(f"The ten times number  is: {result}")
except ValueError:
    print("Oops! That wasn't a valid number. Please enter an integer.")

#SQ4: Find the errors, debug the program, and then execute to show the output.
#Errors
#main() doesn't have :
#Indentation is inconsistent.
#Calories1 vs calories1 → variable name mismatch (Python is case-sensitive).
#Both prompts say “first food” instead of "first" and "second".
#showCalories() is defined with no parameters, but called with (calories1, calories2).
#format() is used incorrectly — needs syntax like format(value, ".2f").
#Inputs are str by default, need to be converted to float or int before addition.
#Didn't call main() function for result

def main():
  calories1 = float(input( "How many calories are in the first food? "))
  calories2 = float(input( "How many calories are in the second food? "))
  showCalories(calories1, calories2)

def showCalories(calories1, calories2): 
  colories = calories1 + calories2
  print("The total calories you ate today: ", format(colories, ".2f"))

#Run program
main()

#Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#         1/30 + 2/29 + 3/28 ............. + 30/1
total = 0
x = 1
y = 30

while x <= 30 and y >= 1:
    total += (x / y)
    x += 1
    y -= 1

print(f"Total sum is: {total}")

'''
Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT
'''
#For example, if the base was 5 and the height was 4, the area would be 10.
#triangle_area(5, 4)   # should print 10

def triangle_area(base,height):
  return 1/2 * base * height

base= float(input("Please enter the base of triangle: "))
height=float(input("Please enter the height of triangle: "))
print(f"Area of the triangle is: {triangle_area(base, height)}")

