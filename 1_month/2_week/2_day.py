# Print the following pattern
# Write a program to print the following number pattern using a loop.

# def  pattern (n):
#     cnt = 0
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         print()
            

# pattern(6)

# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# def suma(n):
#     s = 0
#     for i in range(1,n+1):
#         s += i
#     return s

# n = int(input("Enter number"))
# print("Sum is:",suma(n))

# #Write a program to print multiplication table of a given number

# def multiplication(n):
#     p = 1
#     for i in range(1,n+1):
#         p =i+i
#         if p <= n:
#             print(p)


# multiplication(20)

#Write a program to display all prime numbers within a range
#Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers


# def Prime_Number(start,end):
#     for i in range(start,end+1):
#         cnt = 0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 cnt+=1
#         if cnt == 2:
#           print(i)
          
# start = int(input())
# end = int(input())

# Prime_Number(start,end)


