list = []
for a in range(0,100+1):
    if a % 2 == 0:
        list.append(a)
        print(a)

list.reverse()
for a in list:
    print(a)

    