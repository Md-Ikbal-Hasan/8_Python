print("Pattern Printing: ")
""" 
*
**
***
****
*****
n = 5
for i in range(0,n):
    for j in range(0, i+1 , 1):
        print("*" , end = " ")
    print("\n")
"""

'''
     *
    **
   ***
  ****
 *****
'''
row = 5
for i in range(0,row):
    for j in range(0, row-i-1):
        print(end = " ")

    for k in range(0, i+1):
        
        print("*" , end="")
    
    print(" ")

   






