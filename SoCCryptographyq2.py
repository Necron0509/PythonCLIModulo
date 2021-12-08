
#Q4

import sys
#main menu
def menu():
    print("============ Menu ============= ")
    choice  = input ("""
                    A : Multiplication 
                    B : Power of 
                    C : Addtion 
                    Q : Exit
                    Please enter which modulus type you would like:
                    """)
    if choice == "A" or choice =="a":
        multiplication()
        menu()
    elif choice == "B" or choice == "b":
        power()
        menu()
    elif choice == "C" or choice == "c":
        addtion()
        menu()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You can only select items in the menu")
        print("Please try again")
        menu()


# multiplication function 
#https://www.youtube.com/watch?v=CqaB4B7xzNA
def multiplication():
    print("Please enter a number: /n")
    a = int(input())

    print("\t\t\t Multuplation Mod " + str(a) + "\n")

    for i in range(1,a):
        print(i, end="\t")
    print()
    print("--------------------------------------------------------------------------------------")

    for j in range(1,a):
        for k in range (1,a):
            print((j * k) % a, end="\t")
        print("\n")

  
 # to the power of function 

def power():
    print("Please enter a number: ")
    a = int(input())

    print("\t\t\t Power of Mod " + str(a) + "\n")

    for i in range(1,a):
        print(i, end="\t")
    print()
    print("--------------------------------------------------------------------------------------")

    for j in range(1,a):
        for k in range (1,a):
            print((j**k)%a, end="\t")
        print("\n")

#addtion 

def addtion():
    print("Please enter a number: /n")
    a = int(input())

    print("\t\t\t Addtion Mod " + str(a) + "\n")

    for i in range(1,a):
        print(i, end="\t")
    print()
    print("--------------------------------------------------------------------------------------")

    for j in range(1,a):
        for k in range (1,a):
            print((j + k) % a, end="\t")
        print("\n")

# run program 
if __name__ == "__main__":
    # Launch main menu
    menu()



















