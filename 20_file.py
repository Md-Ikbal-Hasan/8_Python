'''
f = open('a.txt' , 'w') # open file
print("name = " , f.name)
print("is it close? " , f.closed)
print("mode: " , f.mode)
f.write("python is the most powerful language. ")
f.close()
'''

#appending to file
"""  
f = open('a.txt' , 'a')
f.write("C++ is also good languae")
f.write(". java is also")
f.close()
"""

# r+ functionality
""" 
f = open('a.txt' , 'r+')
info  = f.read()
print(info)
f.close()
"""

# w+ functionality
f = open('a.txt' , 'w+')
f.write("all is lost")
f.close()




