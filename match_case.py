#It's looking like switch case statement in C, C++ or Java
#there is no need of break


x = int(input("Enter the number: "))

match x:
    case 0:
        print("X is 0")
    case 1:
        print("case 1")
    case _:         #default case
        print(x)