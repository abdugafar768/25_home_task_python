
# num = input().split()
# n = len(num)
# result = num[::2]

# for i in result:
#     print(i,end=' ')

# ##########################################################
    
# num = input().split()
# for i in num:
#     if int(i) % 2 == 0:
#         print(i,end=' ')

# ##########################################################


# num = input().split()
# cnt = 0
# for i in num:
#     if int(i) > 0:
#          cnt+=1
# print(cnt)

# ###########################################################



# num = input().split()
# n = len(num)
# i = 1

# while i < n:
#     if int(num[i]) > int(num[i - 1]):
#         print(num[i], end=' ')

#     i += 1


# ###########################################################

# num = input().split()
# n = len(num)
# i = 0
# cnt = 0
# while i < n-1:
#     a = num[i]
#     b = num[i+1]
#     if int(a) > 0 and int(b) > 0 or int(a) < 0 and int(b) < 0 :
#         print(a,b)
#         break
#     i += 1

def Problem_conditions(n):
    cnt=-1
    big = -9999999
    for i in n:
        if int(i) > big:
            big = int(i)
            cnt+=1
        
    print(big,cnt)  

list1 = input().split()
Problem_conditions(list1)