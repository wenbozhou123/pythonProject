import re

pattern = '\d\.\d+'
s1 = '我是今天30岁，这个是python3.11'
UNSTARTED = 'u', "Not started yet", 'dsda'
match = re.search(pattern, s1)
print(match)
print(match.span())
print(match.expand('zhou'))
print(match.group())
print(match.endpos)
print(match.end())
print(match.start())
print(match.string)
print('-'*50)
print(UNSTARTED)
print(type(UNSTARTED))

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

