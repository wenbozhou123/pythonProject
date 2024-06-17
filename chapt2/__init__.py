import keyword

print(keyword.kwlist)

i = 0
while i < 5:
    print("while 循环", i)
    i += 1
else:
    print("while循环正常结束!")
print("结束")

for i in range(5):
    print("for循环", i)
    if i == 3:
        break
else:
    print("for循环正常结束!")
print("end")

print(7 << 3)
print(9 >> 3)