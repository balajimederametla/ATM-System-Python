# Initial Data
pin = "0126"
balance = 10000
mini_statement = []
# Function for checking PIN
def authenticate():
    entered_pin = input("Enter Your PIN: ")
    if entered_pin == pin:
        print("\nLogin Successful\n")
        return True
    else:
        print("Incorrect PIN")
        return False
# Main ATM Function
def atm_system():
    global balance, pin, mini_statement
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")
        print("==============================")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            print(f"Current Balance: ₹{balance}")
            mini_statement.append(f"Checked Balance: ₹{balance}")
        elif choice == "2":
            amount = float(input("Enter Deposit Amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} Deposited Successfully")
                print(f"Updated Balance: ₹{balance}")
                mini_statement.append(f"Deposited: ₹{amount}")
            else:
                print("Invalid Amount")
        elif choice == "3":
            amount = float(input("Enter Withdraw Amount: ₹"))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"₹{amount} Withdrawn Successfully")
                    print(f"Remaining Balance: ₹{balance}")
                    mini_statement.append(f"Withdrawn: ₹{amount}")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid Amount")
        elif choice == "4":
            old_pin = input("Enter Old PIN: ")
            if old_pin == pin:
                new_pin = input("Enter New PIN: ")
                confirm_pin = input("Confirm New PIN: ")
                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN Changed Successfully")
                    mini_statement.append("PIN Changed")
                else:
                    print("PIN Mismatch")
            else:
                print("Wrong Old PIN")
        elif choice == "5":
            print("\n------ MINI STATEMENT ------")
            if len(mini_statement) == 0:
                print("No Transactions Yet")
            else:
                for i in mini_statement:
                    print(i)
        elif choice == "6":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid Choice")
# Program Start
if authenticate():
    atm_system()
else:
    print("Access Denied")
