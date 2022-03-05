#use of break
''' 
while True:
    name   = input("Enter your name: ")
    if name == "Ikbal":
        break

print("thank you")

'''

#use of continue
'''  
while True:
    name   = input("Who are you? ")

    if name != "Batman":
        continue

    print("Hello " + name + " what is your passcode?")
    password = input()
    
    if password == 'icecreamtruck':
        print("valid passcode.Now take your icecream")
        break

print("thank you")

'''

#series....
'''   
sum =  0
for i in range(1,5):   # 1+2+3+4 = 10
    sum = sum + i
print(sum)
'''

''''   
sum =  0
for i in range(1,5):   
    sum = sum + i*i
print(sum)
'''

'''  
sum =  0
for i in range(1,10,2): # 1+3+5+7+9
    sum = sum + i
print(sum)
'''



#complex series =  1+ (1+2) + (1+2+3) + (1+2+3+4) = 20
'''  
sum = 0
for i in range(1,5):
    for j in range(1 ,i+1):
        #print(j)
        sum = sum + j

print(sum)
'''




