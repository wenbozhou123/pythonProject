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


