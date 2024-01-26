
list1 = input().split()
big = -9999999
cnt = 0 
for i in list1:
    if int(i) > big:
      big = int(i)
      cnt = i
x = list1.index(cnt)
print(big,x)
####################################################
def Problem_conditions(n):  
    big = +9999999
    for i in n:
        if int(i) > 0:
            if int(i) < big:
              big = int(i) 
    print(big)  

list1 = input().split()
Problem_conditions(list1)

####################################################
def Problem_conditions(n):  
    minn = +9999999
    for i in n:
        if int(i) % 2 != 0:
            if int(i) < minn:
                minn = int(i) 
    if minn == +9999999:
        return 0
    return minn
                
list1 = input().split()
print(Problem_conditions(list1))
####################################################

def Problem_conditions(n1,n2):  
   cnt=1
   for i in n1:
      if int(i) >= n2:
         cnt+=1
         
   return cnt       
list1 = input().split()
number = int(input())
print(Problem_conditions(list1,number))
####################################################
list1 = input().split()
i = 1
cnt = 1
set_list = set(list1)
len_list = len(set_list)
print(len_list)