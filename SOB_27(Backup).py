# Online Video Game Store

'''
For my SOB 27 mini-project, I'll be doing an Online Video Game store.
My plan is to allow users to view the product specs, price, and stock, and give the option to
add things to the cart and remove them.

To fulfill the SOBs requirements, I plan to use while loops, if/else conditions, and for loops
to accomplish this task.
'''

cart = []  # I start by creating a list called "cart" that I'll use to store the user's choices

'''
I have used a dictionary, this is useful as it helps me retrieve and modify data easier,
This is helpful for making my online shop run smoothly for the consumers
'''

games = [
    {"title": "Minecraft", "price": 110.99, "stock": 8},
    {"title": "Dead Space", "price": 298.45, "stock": 5},
    {"title": "Silent Hill", "price": 268.01, "stock": 2}
]  # I have used a dictionary to store the information of my products

'''
I have used a while loop to make the shopping experience more convenient, rather
than having to restart the program over and over. The loop would go through
until the user types in 'exit'. This would help me fulfill the condition of
SOB 28 which I need to require if/else, while and for loops
'''

while True:
    print("\nWelcome to Hani's Arcade Store")
    print("1. View Games")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose an option: ")  # Choice, stores the user's input and runs a specific line of code based upon the user's input

    
    #For Choice "1", I have chosen to display the result
    

    if choice == "1":
        for game in games:
            print(f"{game['title']} - AED {game['price']:.2f} - Stock: {game['stock']}")  # The f function helps us add in-built functions into print statements

    
    #For choice "2", I have given the option to the user to input 
    

    elif choice == "2":
        title = input("Enter a game title: ")
        for game in games:
            if game["title"].lower() == title.lower():  # The .lower() is useful as it can convert all inputs to lowercase avoiding as much errors as possible
                if game["stock"] > 0:  # This if/else condition checks whether there is stock for the items, if not then I'll inform the user that the item isn't in stock
                    cart.append({"title": game["title"], "price": game["price"]})  # This function ".append" is useful as I use it to add a new dictionary into the cart list
                    game["stock"] -= 1  # Updates the stock
                    print(f"{title} added to cart.")
                else:
                    print("Item out of stock.")
                break  # The break function helps end the loop
        else:
            print("Game not found.")

    
    #If the user selects "3", they can remove an item from their cart.
    

    elif choice == "3":
        title = input("Enter the title of the game you wish to remove: ")
        for item in cart:  # This if/else statement checks whether the user has the item in cart before removing it
            if item["title"].lower() == title.lower():  # The .lower() is useful as it can convert all inputs to lowercase avoiding as much errors as possible
                cart.remove(item)  # The .remove() function helps us remove the item from the cart
                
                #This part helps us restore the stock of the removed item
                
                for game in games:
                    if game["title"].lower() == title.lower():
                        game["stock"] += 1  # Adds the stock back
                        break
                print(f"{title} removed from cart.")  # Informs the user the game is removed from the cart
                break
        else:
            print("Game not in cart.")  # Would remind user if the game isn't in the cart

    
    #If the user selects "4", they can view the contents of their cart.
    

    elif choice == "4":
        if not cart:  # This If/else statement checks whether the item is in the cart if not, it would display the below message
            print("Cart is empty.")
        else:
            total = sum(item["price"] for item in cart)  # If there are items in the cart, we use the sum function to calculate the total cost
            print("Cart:")
            for item in cart:
                print(f"{item['title']} - AED {item['price']:.2f}")  # Displays each game in the cart
            print(f"Total: AED {total:.2f}")  # Shows the total price

    
    #If the user selects "5", they can proceed to checkout.
    

    elif choice == "5":
        if cart:  # This if/else statement ensures there are items in the cart before checkout.
            print("Checkout successful!")
            cart.clear()  # This would clear out the cart
        else:
            print("Cart is empty.")

    
    #If the user selects "6", exit the store.
    
    
    elif choice == "6":
        print("Goodbye!")
        break
    
    
    #If the user enters an invalid choice, display an error message.
    
    
    else:
        print("Invalid choice.")


                       
                      

    
