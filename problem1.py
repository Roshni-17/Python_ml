num=int(input("Enter a number = "))
if(num%2==0):
    if(num>=2 and num<=5):
        print("Not weird")
    elif(num>=6 and num<=20):
        print("weird")
    else:
        print("Not weird")
else:
    print("weird")