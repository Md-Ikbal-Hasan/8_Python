def test():
  x = 200  # local variable
  print(x)

test()
# print(x)   # can not access x here. x is local

y = 220
def test2():
  x = 210
  print(x)
  print(y) # y can be access , y is global varibale

test2()




def myfunc():
  x = 300  # local variable
  print(x)

myfunc()





def myfunc2():
  x = 420
  def myinnerfunc():
    print("inner function: " , x)  # can access x. because myinnerfucn is an inner function and x is a varibale of its outer function
  myinnerfunc()

myfunc2()



