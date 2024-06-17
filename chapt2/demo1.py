print("hello, python")
for i in range(10):
    print(i)
print(not False)

fd = open("test.txt", "w")
print("你好，python！", file=fd)
fd.close()

fd = open("test.txt", "r")
print("读", fd.read())
fd.close()
