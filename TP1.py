
#Exercise 1: Basic Data Types and Operators

# A = int(input("Enter the nombere A : "))
# B = int(input("Enter the nombere B : "))

# print("\n The addition betweene A and B is : " ,  A+B )
# print("\n The subtraction betweene A and B is : " , A-B )
# print("\n The multiplication betweene A and B is : " , A*B )
# print("\n Division A / B is : " , A/B )

# if(A > B):
#     print( f"\n The first number({A}) is greater than to the second number({B})" )
# if(A < B):
#     print( f"\n The first number({A}) is less than to the second number({B})" )
# if(A ==B ):
#     print( f"\n The first number({A}) is equal to the second number({B})" )

#Exercise 2: Control Flow

# x = int(input("Enter a number : "))

# if( (x%3)==0 and (x%5)==0 ):
#     print("FizzBuzz")
# elif( (x%3)==0 ):
#     print("Fizz")
# elif( (x%5)==0 ):
#     print("Buzz")
# else:
#     print(x)


# Exercise 3: Lists and Loops

# L = [12,99,34,53,28,76,65,93,22,1]
# print(L)

# sumList = 0
# for i in L :
#     sumList = sumList + i 
# print("The sum of all numbers in the list is : ", sumList )

# print("The maximum values in the list : " , max(L) )
# print("The minimum values in the list : " , min(L) )

# newL = []
# for i in L :
#     if( i%2 == 0 ):
#         newL.insert(1,i)
# print("The even numbers is : ", newL)

#Exercise 4: Functions

# def calculate_factorial(z):
#     if(z < 0 ):
#         print("ERORR Negative Number ")
#     else:
#         fac = 1
#         for i in range(1, z + 1):
#             fac = fac*i
#         return fac 

# z = int(input("Enter a number : "))
# print(calculate_factorial(z))


# Exercise 5: Dictionaries

phone_book = {}

while True:
    print("\n1. Add Contact\n2. Look Up Contact\n3. Delete Contact\n4. Show All Contacts\n5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print(f"Added {name}.")

    elif choice == '2':
        name = input("Enter name to look up: ")
        if name in phone_book:
            print(f"{name}'s number is {phone_book[name]}")
        else:
            print("Contact not found.")

    elif choice == '3':
        name = input("Enter name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Deleted {name}.")
        else:
            print("Contact not found.")

    elif choice == '4':
        if phone_book:
            for name, number in phone_book.items():
                print(f"{name}: {number}")
        else:
            print("Phone book is empty.")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")


