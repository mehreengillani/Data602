'''Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
'''
class BankAccount:
  def __init__(self, bankname, firstname, lastname, balance=0):
    self.bankname = bankname
    self.firstname = firstname
    self.lastname = lastname
    self.balance = balance
    
# A method called deposit() that allows the user to make deposits into their balance.    
  def deposit(self, deposit_amount): 
    #update balance
    self.balance +=deposit_amount
    print(f"{deposit_amount} deposited. New balance: {self.balance}\n")
    
# A method called withdrawal() that allows the user to withdraw from their balance.
  def withdrawal(self, withdraw_amount):
  # Withdrawal may not exceed the available balance. Hint: consider a conditional argument in withdraw() method 
    if withdraw_amount > self.balance:
      print("You can't withdraw this amount. Your Balance is low. Try another amount: \n")
    else:
      # update balance
      self.balance -= withdraw_amount
      print(f"{withdraw_amount} withdrawn. Remaining balance: {self.balance}\n")
      
# Use the __str__() method in order to display the bank name, owner name, and current balance
  def __str__(self):
    return f"Bank: {self.bankname}\nOwner: {self.firstname} {self.lastname}\nBalance: {self.balance}\n"

# Make a series of deposits and withdrawals to test your class.
#create instances
accountholder1= BankAccount("TP Bank", "David", "John", 1200)
accountholder2= BankAccount("Standard Chartered Bank", "Alis", "Ben", 5000)

#Perform withdrawals
accountholder1.withdrawal(200)
accountholder2.withdrawal(300)

#Perform deposits
accountholder1.deposit(1400)
accountholder2.deposit(260)

# Display account info
print(accountholder1)
print(accountholder2)
'''
Q2: Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create…
'''
import math
class Box:
  def __init__(self,length,width):
    self.length = length
    self.width = width
    
# A method called render() that prints out to the screen a box made with asterisks of
#length and width dimensions
# Render method to print a box of asterisks
  def render(self):
    for i in range(self.length):
      print('*' * self.width) # print 'width' asterisks per row
# A method called invert() that switches length and width with each other
  def invert(self):
    self.length = self.width
    self.width = self.length

#Methods get_area() and get_perimeter() that return appropriate geometric calculations
  def get_area(self):
    area = self.length * self. width
    return f"Area of the box is: {area}\n"
  def get_perimeter(self):
    perimeter = 2 * (self.length + self.width)
    return f"perimeter of the box is: {perimeter}\n"
#A method called double() that doubles the size of the box. Hint: Pay attention to return
#value here. 
  def double(self):
    self.length = self.length * 2
    self.width = self.width * 2
    return f"The new length of the box is: {self.length} \n The new width of the box is: {self.width}\n"

# Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
#their respective lengths and widths are identical.
# Compare two boxes
  def __eq__(self, other):
    return self.length == other.length and self.width == other.width

#A method print_dim() that prints to screen the length and width details of the box
  def print_dim(self):
    print(f"The length of the box is: {self.length}")
    print(f"The width of the box is: {self.width}\n")
    
#A method get_dim() that returns a tuple containing the length and width of the box
  def get_dim(self):
    # Return the dimensions as a tuple
    return (self.length, self.width)
  
# A method combine() that takes another box as an argument and increases the length
#and width by the dimensions of the box passed in
  def combine(self, box):
    self.length += box.length
    self.width += box.width
    return (self.length, self.width)

#A method get_hypot() that finds the length of the diagonal that cuts through the middle
  def get_hypot(self):
  # Calculate the diagonal (hypotenuse)
    digonal = math.sqrt(self.length**2 + self.width **2)
    return digonal

#Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
#box2 and box3 respectively
box1= Box(5,10)      
box2 = Box(3,4)
box3 = Box(5,10)

#Print dimension info for each using print_dim()
box1.print_dim()
box2.print_dim()
box3.print_dim()

# Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
#screen accordingly
print(f"box1 == box2: {box1 == box2}")
print(f"box1 == box3: {box1 == box3}")

# Combine box3 into box1 (i.e. box1.combine())
box1.combine(box3)

# Combine box2 into box1
box1.combine(box2)
#print new diemnsion of box1
box1.print_dim()

# Double the size of box2
box2.double()
box2.print_dim()
 
  

