userAccount = {
    "name": "User Name",
    "surname": "User Surname",
    "number": 5555555555,
    "balance": 10000,
    "overdraft": 5000  # ek hesap
}

def withdrawMoney(account):
    amount = float(input("Enter the amount of money you want to withdraw: "))

    if (account["balance"] >= amount):
        print("You have withdrawn the money from your account")
        newBalance = account["balance"] - amount
        account.update({"balance": newBalance})
        print(f"Remaining balance = {account['balance']}")
    
    else:
        total = account["balance"] + account["overdraft"]
        if total >= amount:
            useOverdraft = input("Would you like to use your overdraft account? y/n: ")
            if useOverdraft == "y":
                print("Withdrawal process completed.")
                remainingAmount = amount - account["balance"]                
                account.update({"balance": 0})
                print(f"Remaining balance = {account['balance']}")
                
                newOverdraft = account["overdraft"] - remainingAmount
                account.update({"overdraft": newOverdraft})
                print(f"Remaining overdraft balance = {account['overdraft']}")

            elif useOverdraft == "n":
                print("The amount entered is insufficient in your balance.")

            else:
                print("The value you entered has no result here.")

        else:
            print("The money you want to withdraw is not available in your account.")

# Loop logic
loopCount = int(input("How many times do you want the loop to run: "))
for x in range(loopCount):
    withdrawMoney(userAccount)