# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
hotdog_cost = 0
pepper_cost = 0
cheese_cost = 0
grilled_onion_cost = 0

hotdog = (input("Do you want a Hotdog or Chilidog: "))
if hotdog == "Hotdog":
        hotdog_cost = 3.50
if hotdog == "Chilidog":
        hotdog_cost = 4.50

cheese = (input("Do you want Cheese, Yes or No: "))
if cheese == "Yes":
    cheese_cost = +.5
elif cheese == "No":
    cheese_cost = +0

peppers = (input("Do you want Peppers, Yes or No: "))
if peppers == "Yes":
    pepper_cost = +.75
elif peppers == "No":
    pepper_cost = +0

grilled_onions = (input("Do you want Grilled Onions, Yes or No: "))
if grilled_onions == "Yes":
    grilled_onion_cost = +1
elif grilled_onions == "No":
    grilled_onion_cost = +0
topping_cost = pepper_cost + grilled_onion_cost + cheese_cost
Value = topping_cost + hotdog_cost
Tax = 0.07 * Value
total_cost = Value + Tax
print("Your Hot dog costs", Value)
print("Your tax is", Tax)
print("Your total is", total_cost)
