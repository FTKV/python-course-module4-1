str1 = ", "

lst1 = [str(x) for x in range(10)]

str2 = str1.join(lst1)

print(str2)

str1 = ", "

lst1 = [x for x in range(10)]

str2 = str1.join(str(x) for x in lst1)

print(str2)