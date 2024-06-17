list1 = [88, 89, 99, 00, 98]
print(list1)
res_list=[]
for i in range(len(list1)):
    if 0 == list1[i]:
        res_list.append("200" + str(list1[i]))
    else:
        res_list.append("19" + str(list1[i]))
print(res_list)

res_list.clear()

for index, value in enumerate(list1):
    if 0 == value:
        res_list.append("200" + str(value))
    else:
        res_list.append("19" + str(value))
print(res_list)