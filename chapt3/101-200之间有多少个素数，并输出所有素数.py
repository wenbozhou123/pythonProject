import math

# 101-200之间有多少个素数，并输出所有素数
# print(range(20**0.5))
lst=[]
for i in range(101, 201):
    flag = False  # 是否为合数
    for j in range(2, math.ceil(i**0.5)+1):
        if i % j == 0:
            flag = True
            break
    if not flag:
        lst.append(i)
print(lst)