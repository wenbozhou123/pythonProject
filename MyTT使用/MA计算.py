from MyTT import *                 # 声明调用MyTT， 请注意大小写
S = np.random.randint(1, 99, [10])      # 生成1-99内的10个数序列
EMA(S, 6)                       # 对这个序列S进行6周期EMA指数平均计算
print(S)
print(EMA(S, 6))
print(len(EMA(S, 6)))
print(", ".join(map(str, MA(S, 6))))

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [1,2]
print(*nested_list)
print(zip(*nested_list))
print(*lst)

print([*lst])
#print(map(list, zip(*lst)))
