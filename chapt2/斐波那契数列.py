# 斐波那契数列
lst1=[0, 1]
num = 30
for i in range(2, num):
    lst1.append(lst1[i-1]+lst1[i-2])

print(lst1)

print(1, 'oo')