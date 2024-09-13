lst1=[]
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != i:
                total = i * 100 + j * 10 + k
                lst1.append(total)

print(lst1)