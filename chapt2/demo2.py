import json
name = "zhoubowen"
out = f"myname is Hello {name} "
# mycmd=input("请输入命令")
#eval(mycmd)
print(out)
# 生成一个文件
# fd = open("myname.txt", "w")

listStr = '["all","kl","all","out"]'
list1 = json.loads(listStr)
print(list1)
print(type(list1))
print(list1)
print(list1.append("hello"))
print(bool(list1.append("hello")))
print(list1)

seen = set()
unique_list = [x for x in list1 if not (x in seen or seen.add(x))]
print(unique_list)
print([x for x in range(10)])
search = 'ut'
if any(search in e for e in list1):
    print(search)
