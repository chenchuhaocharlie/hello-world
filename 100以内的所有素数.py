p = [2, ]
temp = " "
for i in range(2, 101):
    for temp in range(2, i):
        if i % temp == 0:
            break
    if temp == i-1:
        p.append(i)
print(p)
