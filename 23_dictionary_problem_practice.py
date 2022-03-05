"""
import pprint as pp # for sorted print....
# find out frequency of  character
text = 'this is simple text to TEST the code.'
letters = {}

for i in text:
    letters.setdefault(i , 0)
    letters[i] = letters[i] + 1

pp.pprint(letters)
"""

"""  
# password protected app access
password_bank = {'Sam':1234 ,'Smith':909090 ,'Ruth':120987}
matched = False
x = 0# loop control variable

print("Enter your name: ")

while x<5:
    name = input()
    if name in password_bank:
        for i in range(0,3):
            print("Enter Your Password")
            password = int(input())
            if password in password_bank.values():
                matched = True
                print("Access granted")
                break
            else:
                if i==2:
                    continue
                else:
                    print("Wrong password. Try again . You have " + str(2 - i) + " tries left")





    else:
        print("There is no such name in the password bank. Try again")

    x = x+1

    if matched:
        break
    if i == 2:
        print("Sorry. Wrong Password is entered lots of time. Try again after 1 Hour.")
        break

"""

# simulate a phone book
contact_no  ={'Ikbal':'0187', 'Sunny':'0175', 'Alhaj':'0198'}
x = 0
while x<5:
    print("Enter your name (press enter to exit..) : ")
    name  = input()

    if name == "":
        break
    if name in contact_no:
        print("The contact number of " + name + " is " + str(contact_no[name]))
    else:
        print("There is no such name in phoneBook. Do you want to add it(yes / no) : ")
        desc = input()
        if desc == 'yes':
            num = input("Enter the number: ")
            contact_no[name] = num
            print("Phone book updated. seacrh again")
        elif desc == 'no':
            desc = input("Do you want to quite? ")
            if desc == 'yes':
                break
            else:
                print("Keep searching....")

    x = x+1













