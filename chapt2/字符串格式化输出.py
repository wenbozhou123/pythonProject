print('-'*50)
number = 1234.56789
print(f"{number:.2f}")     # 保留两位小数
print(f"{number:,.2f}")    # 保留两位小数并使用千位分隔符
print(f"{number:.0f}")     # 不保留小数
print(f"{number:08.2f}")   # 保留两位小数，总宽度为 8，使用 0 填充

print('-'*50)
text = "Hello"
print(f"{text:>10}")  # 右对齐，宽度为 10
print(f"{text:<10}")  # 左对齐，宽度为 10
print(f"{text:^10}")  # 居中对齐，宽度为 10

print('-'*50)
text = "Hello"
print(f"{text:*>10}")  # 右对齐，宽度为 10，*号填充
print(f"{text:*<10}")  # 左对齐，宽度为 10，*号填充
print(f"{text:*^1}")  # 居中对齐，宽度为 10，*号填充

print('str.format()', '-'*50)
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {name}, Age: {age}".format(name=name, age=age))

print('f-strings', '-'*50)
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")



