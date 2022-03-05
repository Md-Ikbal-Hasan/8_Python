# Banking system
bank_users = {'Ikbal': 120000, 'Sunny':100000, 'Alhaj':150000}
print("....Welcome to Banking System....")

while True:
    print('  ' + '1. View Balance')
    print('  ' + '2. View All User Info')
    print('  ' + '3. Update Balance')
    print('  ' + '4. Exit')

    desc = input('What do you like to do? : ')
    if desc == '1':
        k = input("Enter user Name, Please: ")
        if k in bank_users.keys():
            print(k+ "'s Bank balance is :  " + str(bank_users[k]))
        else:
            desc = input("User not found. Would you like to add the user to the account(YES / NO) : ")
            if desc == 'YES':
                k = input("Enter name,please : ")
                v = input("Enter balance,please : ")
                bank_users.update({k:v})
            else:
                desc = input("Would you like to exit? ")
                if desc == 'YES':
                    break
    elif desc == '2':
        for k,v in bank_users.items():
            print("Username => " + str(k) + " Bank Balance : " + str(v))

    elif desc == '3':
        k = input("Enter Your Name, Please: ")
        if k in bank_users.keys():
            desc = input("ADD balanace or SUBTRACT balance: ")
            if desc =='ADD':
                temp_balance = bank_users[k]
                extra = int(input("Enter the amount that you want to add: "))
                bank_users[k] = temp_balance +  extra
                print("Balance updated. Current balance is : " , bank_users[k])
            else:
                temp_balance = bank_users[k]
                extra = int(input("Enter the amount that you want to subtract: "))
                bank_users[k] = temp_balance - extra
                print("Balance updated. Current balance is : " , bank_users[k])
        else:
            print("There is no such accout in Database.")

    elif desc == '4':
        break





