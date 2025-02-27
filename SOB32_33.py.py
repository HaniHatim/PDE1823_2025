# Online Video Game Store

'''
For my SOB 32 & 33, I have planned to design a surprise discount for the user between 5% and 20%.

To fulfill the requirements for the SOB, I have used the def functions to store my commands where I can
recall them at any point of the code for efficiency.

As for SOB 33, where I need to add an imported library, I have chosen random. My plan is to create
a program in which the user would receive a surprise discount to enhance customer experience.

###SOB 33: Describe how the interpreter/compiler 'imports'.###

In Python, the import statement allows us to use external modules and libraries in our code.
When we import a module, Python first checks if it is a built-in module, then searches for it in the system’s directories.
If found, it loads the module into memory, compiles it if necessary, and executes its code.
This allows us to access predefined functions and features without writing everything from scratch.
'''

# Importing the random module to generate random discount percentages
import random  # This allows us to use specialized functions like generating random numbers

cart = []  # List to store the user's selected games

games = [
    {"title": "Minecraft", "price": 110.99, "stock": 8},
    {"title": "Dead Space", "price": 298.45, "stock": 5},
    {"title": "Silent Hill", "price": 268.01, "stock": 2}
]  # Dictionary storing game details

def display_games():
    for game in games:
        print(f"{game['title']} - AED {game['price']:.2f} - Stock: {game['stock']}")

def add_to_cart(title):
    for game in games:
        if game["title"].lower() == title.lower():
            if game["stock"] > 0:
                cart.append({"title": game["title"], "price": game["price"]})
                game["stock"] -= 1  # Updates the stock
                print(f"{title} added to cart.")
            else:
                print("Item out of stock.")
            return  # Ends function execution after adding item
    print("Game not found.")

def remove_from_cart(title):
    for item in cart:
        if item["title"].lower() == title.lower():
            cart.remove(item)
            for game in games:
                if game["title"].lower() == title.lower():
                    game["stock"] += 1  # Restores stock
                    break
            print(f"{title} removed from cart.")
            return
    print("Game not in cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
    else:
        total = sum(item["price"] for item in cart)
        print("Cart:")
        for item in cart:
            print(f"{item['title']} - AED {item['price']:.2f}")
        print(f"Total: AED {total:.2f}")

# I have added the def function for the suprise discount upon checkout
def checkout():
    if cart:
        total = sum(item["price"] for item in cart)  # Calculate total price
        discount_percentage = random.randint(5, 20)  # Generate a discount between 5% and 20%
        discount_amount = (discount_percentage / 100) * total  # Calculate discount amount
        final_total = total - discount_amount  # Apply discount

        print(f"Original Total: AED {total:.2f}")
        print(f"Congratulations! You got a {discount_percentage}% discount!")
        print(f"Discounted Total: AED {final_total:.2f}")
        print("Checkout successful! Thank you for your purchase.")
        
        cart.clear()  # Clears the cart after purchase
    else:
        print("Cart is empty.")

while True: # We call our functions within the while loop
    print("\nWelcome to Hani's Arcade Store")
    print("1. View Games")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")  

    choice = input("Choose an option: ")

    if choice == "1":
        display_games()
    elif choice == "2":
        title = input("Enter a game title: ")
        add_to_cart(title)
    elif choice == "3":
        title = input("Enter the title of the game you wish to remove: ")
        remove_from_cart(title)
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":  
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

