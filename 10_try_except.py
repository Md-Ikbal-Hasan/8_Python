def func(x):
    try:
        return 100/x
    except:
        return "There is a zero division error"



ans = func(0)
print(ans)