def countdown(i):
    print(i)
    if i <= 0:
        return
    countdown(i - 1)

def factorial(i):
    if i <= 1:
        return 1
    
    res = i * factorial(i - 1)
    print(res)
    return res
    

countdown(4)
print()
res = factorial(5)
print(res)