"""this program allows user to choose pizza toppings.
Author: Abdalla Farah
Date: 02/26/2026
"""
#create an empty list to store pizza toppings
pizza_toppings: list[str] = []

active: bool = True
#prompt the user to enter pizza toppings until they choose to quit
while active:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").strip()
    if topping.lower() == 'quit':       
        active = False
        
#validate the input to ensure only letters are accepted as toppings
    elif not topping.replace(" ", "").isalpha():
        print("Invalid input. Please enter a valid pizza topping.")
        
#if the input is valid, add the topping to the list and print a confirmation message        
    else:
        pizza_toppings.append(topping)
        print(f"I will add {topping} to your pizza.")