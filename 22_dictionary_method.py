identity = {'Name':'Ikbal' , 'Age':'23','Job':'Software Engineer'}

for i in identity.values():
   print('values: ' , i)

for i in identity.keys():
   print('keys: ' , i)


for i in identity.items():
    print('item: ' ,i)


x = list(identity.keys())
y = list(identity.values())
print(x)
print(y)


for k,v in identity.items():
    print(k ," ", v)

# check key is present or not.....
print("Name" in identity.keys())  # check key is present or not..   True
print("Email" in identity)  # False

print("Ikbal" in identity.values())  # True
print("Rahim" in identity.values())  # Flase
print("Age" in identity.keys())  # True


# get(key , value/default_value) method..
#if key is present then show the corresponding value otherwise show default value
print(str(identity.get('Name' ,'Default')))
print(str(identity.get('Height' ,'Default')))
print(str(identity.get('Name')))
print(str(identity.get('Nameeee')))

print(identity)

# setdefault()  method
print(identity.setdefault('Name','Shaon'))
print(identity.setdefault('Height','5feet'))
print(identity)








