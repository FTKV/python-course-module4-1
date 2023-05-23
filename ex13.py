str1 = "Hello"

print(str1[-1])

str1 = str1.replace("H", "")

print(str1)

print(str1[-2:-1])

str2 = "Hello World"

print(str2.startswith("Hell"))

print(str2.startswith("World"))

print(str2.startswith("Wor", 6))

print(str2.endswith("rld"))

print(str2.endswith("rl"))

print(str2.endswith("ld", -2))