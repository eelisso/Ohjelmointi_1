list = []
print("Give 5 numbers:")
for a in range(5):
    num = int(input("Next number: "))
    list.append(num)


print("The numbers you entered that were greater than zero were:")
for a in list:
    if a > 0:
        print(a)




