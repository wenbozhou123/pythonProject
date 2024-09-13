import copy

# 创建一个嵌套的列表
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 浅拷贝
shallow_copy = copy.copy(original_list)

# 深拷贝
deep_copy = copy.deepcopy(original_list)

# 修改原始列表中的元素
original_list[0][0] = 'Changed'

print("Original list:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
