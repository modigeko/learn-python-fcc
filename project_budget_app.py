class Category:
  def __init__(self, name):
    self.name = name
    self.balance = 0.0
    self.ledger = []

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def __str__(self):
    output = self.name.center(30, '*')
    for entry in self.ledger:
      output += "\n" + f"{entry['description'][:23]:<23}{entry['amount']:7.2f}"
    output += "\n" + f"Total: {self.balance:.2f}"
    return output

def create_spend_chart(categories):
    title = "Percentage spent by category"
    # get total withdrawals from each category
    spent_list = []
    total_withdrawals = 0
    for category in categories:
      withdrawals = 0
      for entry in category.ledger:
        if entry['amount'] < 0:
          withdrawals += entry['amount']
      spent_list.append(abs(int(withdrawals)))
    total_withdrawals = sum(spent_list)
    percent_list = []
    if total_withdrawals == 0:
      percent_list = [0] * len(spent_list)
    else:
      percent_list = [(((item * 100) // total_withdrawals) // 10) * 10 for item in spent_list]

    # print(spent_list, total_withdrawals, percent_list)
    y_axis = ""
    for i in range(100, -1, -10):
      y_axis += f"\n{str(i):>3}| "
      for category in percent_list:
        if category >= i:
          y_axis += "o  "
        else:
          y_axis += "   "
    horizontal_line = "\n" + ' ' * 4 + "".center(len(categories) * 3 + 1, '-')

    # return if the list is empty
    if len(categories) < 1:
      return title + y_axis + horizontal_line

    # populate categories into a list
    category_list = []
    for category in categories:
      category_list.append(category.name)

    # get the longest length of the category name
    max_length = max(len(s) for s in category_list)

    # vertical_view list to hold each row
    vertical_view = []

    # num of spaces to add on the left side
    left_padding = 5

    # num of spaces after each element
    spaces_after_element = 2

    # populate the vertical_view list with rows
    for i in range(max_length):
        row = []
        for category in category_list:
            if i < len(category):
                row.append(category[i])
            else:
                row.append(' ')
        # Join characters with spaces and add padding
        vertical_view.append(' ' * left_padding + '  '.join(row) + ' ' * spaces_after_element)

    # Join all rows with newlines and print the result
    x_axis = '\n' + '\n'.join(vertical_view)

    return title + y_axis + horizontal_line + x_axis


# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)

# categories = [food, clothing]
# print(create_spend_chart(categories))

import random
food = Category("Food")
food.deposit(random.randint(100, 1000), "initial deposit")
food.withdraw(random.randint(10, 100), "groceries")
food.withdraw(random.randint(10, 100), "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(random.randint(100, 1000), "initial deposit")
clothing.withdraw(random.randint(10, 100), "shirts")
clothing.withdraw(random.randint(10, 100), "pants")

auto = Category("Auto")
auto.deposit(random.randint(100, 1000), "initial deposit")
auto.withdraw(random.randint(10, 100), "gas")
auto.withdraw(random.randint(10, 100), "maintenance")

print(create_spend_chart([food, clothing, auto]))





"""
Build a Budget App Project
Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'. The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'. If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
When the budget object is printed it should display:

A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total.
Here is an example usage:

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
Note: open the browser console with F12 to see a more verbose output of the tests.

Run the Tests (Ctrl + Enter)
Save your Code
Reset this lesson
Get Help
Tests
Waiting:The deposit method should create a specific object in the ledger instance variable.
Waiting:Calling the deposit method with no description should create a blank description.
Waiting:The withdraw method should create a specific object in the ledger instance variable.
Waiting:Calling the withdraw method with no description should create a blank description.
Waiting:The withdraw method should return True if the withdrawal took place.
Waiting:Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33.
Waiting:Calling the transfer method on a category object should create a specific ledger item in that category object.
Waiting:The transfer method should return True if the transfer took place.
Waiting:Calling transfer on a category object should reduce the balance in the category object.
Waiting:The transfer method should increase the balance of the category object passed as its argument.
Waiting:The transfer method should create a specific ledger item in the category object passed as its argument.
Waiting:The check_funds method should return False if the amount passed to the method is greater than the category balance.
Waiting:The check_funds method should return True if the amount passed to the method is not greater than the category balance.
Waiting:The withdraw method should return False if the withdrawal didn't take place.
Waiting:The transfer method should return False if the transfer didn't take place.
Waiting:Printing a Category instance should give a different string representation of the object.
Waiting:create_spend_chart should print a different chart representation. Check that all spacing is exact.
"""