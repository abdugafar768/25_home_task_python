num = input().split()
n = len(num)
i = 0
while i < n:
    if int(num[i]) > 0 and int(num[i + 1] > 0):
        print(num[i],num[i+1])

    i += 1