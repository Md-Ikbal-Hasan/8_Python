"""
# old way of string formatting => C style
print("I am %s and I am %d years old" %('Ikbal' , 23)   )

name = "Ikbal"
age  = 23
profession = "web Developer"
earning  = 1050.5012334
print("I am %s. I am %d years old. I am a %s and I earn %.2f$ " %(name,age,profession,earning))
"""


""" 
# .formate style . It is slicely better way
print('I am {} and I am {}' .format('Ikbal','Happy'))
name = "Ikbal"
print('I am {1} and I am {0}' .format(name,'Happy'))
"""

#much better formatting for string
name = "Ikbal"
language = "Java"
print(f"I am {name}. I don't believe in {language} and {2*2} = {4}")
print(f"I am Ikbal. Web developer")













