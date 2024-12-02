def decor(num):
    def inner(num):
        return num + 3
    result = inner(num)  
    return result
decor(3)
print(decor(3))

