#It's looking like switch case statement in C, C++ or Java
#there is no need of break
# we can use 3 default cases

x = int(input("Enter the number: "))

match x:
    case 0:
        print("X is 0")
    case 1:
        print("case 1")

    case _ if x!=10:
        print(x, "is not 20")
    case _ if x!=20:
        print(x, "is not 10")
    case _:         #default case
        print(x)