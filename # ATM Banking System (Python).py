# ATM Banking System (Python)

print("===== Welcome to ATM =====")

balance = 1000  # initial balance

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your Balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance -= amount
            print("Withdrawal successful!")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Please try again.")