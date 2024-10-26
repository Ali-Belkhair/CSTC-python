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

L = [12,99,34,53,28,76,65,93,22,1]
print(L)

sumList = 0
for i in L :
    sumList = sumList + i 
print("The sum of all numbers in the list is : ", sumList )

print("The maximum values in the list : " , max(L) )
print("The minimum values in the list : " , min(L) )

newL = []
for i in L :
    if( i%2 == 0 ):
        newL.insert(1,i)
print("The even numbers is : ", newL)


