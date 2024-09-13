# 一个正整数分解质因数
num = 90
i = 1
lst=[]
while i < num:
    if num % i == 0:
        lst.append(i)
        num = num // i
    i+=1
print(lst)