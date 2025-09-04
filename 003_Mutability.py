# 'int' & 'str' types are immutable
x = 10
print(id(x))

x = 20
print(id(x))


s1 = "Test"
print(f"{id(s1) = }")

print(s1[0])

# s1[0] = "B"
# s1 = "Best"; print(s1)

lst1 = list(s1)
print(f"{id(lst1) = }")
lst1[0] = "B"
print(lst1)
print(f"{id(lst1) = }")
print(type(s1), s1)
s1 = "".join(lst1)
print(type(s1), s1)
print(f"{id(s1) = }")

for x in s1:
    print(x, end="-")
print()