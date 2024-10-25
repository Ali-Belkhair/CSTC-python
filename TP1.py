#Exercice 1:

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

#Exercice 2:

x = int(input("Enter a number : "))

if( (x%3)==0 and (x%5)==0 ):
    print("FizzBuzz")
elif( (x%3)==0 ):
    print("Fizz")
elif( (x%5)==0 ):
    print("Buzz")
else:
    print(x)
