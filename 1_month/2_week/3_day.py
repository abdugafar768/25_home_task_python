# def Add(a, b):
#     print(a + b)

# def Subtract(a, b):
#     print(abs(a - b))

# def Multiply(a, b):
#     print(a * b)

# def Division(a, b):
#     print(a // b)
# num = input().split()
# a = int(num[0])
# b = int(num[1])
# Add(a, b)
# Subtract(a, b)
# Multiply(a, b)
# Division(a, b)


# def Min(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# num_string = input().split()
# a = int(num_string[0])
# b = int(num_string[1])
# print(Min(a,b))


# def Abs(a):
#     if a > 0:
#         return a
#     else:
#         return -a
# a = int(input())
# print(Abs(a))


# def EvenOrOdd(a):
#     if a % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
# a = int(input())
# print(EvenOrOdd(a))


# def Max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num_string = input().split()
# a = int(num_string[0])
# b = int(num_string[1])
# print(Max(a,b))

# def MinDigit(a):
#     m = 9
#     mx = -1
#     for i in a:
#         if int(i) < m:
#             m = int(i)
#         if int(i) > mx:
#             mx = int(i)
#     return mx+m
# a = input()
# print(MinDigit(a))
    

# def FindMin(a,b,c,d):
#     if a < b and a < c and a < d:
#         return a
#     elif b < a and b < c and b < d:
#         return b
#     elif c < a and c < b and c < d:
#         return c
#     else:
#         return d
# num_string = input().split()
# a = int(num_string[0])
# b = int(num_string[1])
# c = int(num_string[2])
# d = int(num_string[3])
# print(FindMin(a,b,c,d))


# def Pow(x,y):
#     daraja = 1
#     for i in range(1,y+1):
#         daraja *= x
#     return daraja
     
# num = input().split()
# a = int(num[0])
# b = int(num[1])
# print(Pow(a,b))


# def Sqrt(a):
#     for i in range(1,a+1):
#         if i * i == a:
#             return i
# a = int(input())
# print(Sqrt(a))

# def Divisors(a):
#     cnt = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             cnt+=1
#     return cnt
# a = int(input())
# print(Divisors(a))

