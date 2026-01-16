import random
print("""
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""")


cards = [1,11,2,3,4,5,6,7,8,9,10,10,10,10]

# Computer cards
computer_total = random.choice(cards) + random.choice(cards)
print(f"Computer total: {computer_total}")

# User cards
user_total = random.choice(cards) + random.choice(cards)
print(f"User total: {user_total}")

# Ask user to draw another card
if user_total < 21:
    ask = input("Do you want another card? (yes/no): ").lower()

    if ask == "yes":
        user_total += random.choice(cards)
        print(f"User new total: {user_total}")

    else:
        computer_total += random.choice(cards)
        print(f"Computer new total: {computer_total}")

# Final result
if user_total > 21:
    print("Computer wins")
elif computer_total > 21:
    print("User wins")
elif user_total == 21:
    print("User wins with 50% bonus")
elif user_total > computer_total:
    print("User wins")
else:
    print("Computer wins")



