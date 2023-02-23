def collection(x,y):
    return x+y

def extraction(x,y):
    return x-y

def crash(x,y):
    return x*y

def division(x,y):
    return x/y

print("select the action to be performed")
print("-------------------")
print("1.collection")
print("2.extraction")
print("3.crash")
print("4.division")

choice= input("your choice(1/2/3/4):")

number1=int(input("1. number: "))
number2=int(input("2. number: "))


if choice=='1':
    print(number1,"+",number2,"=", collection(number1,number2))

elif choice=='2':
    print(number1,"-",number2,"=", extraction(number1,number2))

elif choice=='3':
    print(number1,"*",number2,"=", crash(number1,number2))

elif choice=='4':
    print(number1,"/",number2,"=", division(number1,number2))
else:
    print("invalid login")