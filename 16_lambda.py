#lambda parameter : expression pasees_parameter

print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

res = (lambda a,b : a*a + 2*a*b + b*b) (2,3)
print(res)

square  = (lambda x : x*x)
r = square(4)
print(r)

cube = (lambda x : x*x*x)(2)
print(cube)

cube2 = (lambda x : x*x*x)
result  = cube2(3)
print(result)