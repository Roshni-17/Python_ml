def swapi(x):
    k = ''
    for i in x:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    return k
st = input("enter the string")
ret = swapi(st)
print(ret)



