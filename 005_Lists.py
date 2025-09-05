# LIST 
## Mutable collection of non-homgeneous elements

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

lst = [1, 2, 3, "Manish", "Abhijeet", add]

print(lst[0])

print(lst[3])

res = lst[-1](2, 3)
print(res)

print(lst)

lst.append(sub)
print(lst)

print(lst[-1](7, 5))



l1 = [1, 2, 3, 4, 5]
l2 = []
l3 = list()

s1 = "Test"
for c in s1:
    print(c, end=" - ")
print()

l4 = list(s1)
print(l4)

# l1B = l1[:]
l1B = list(l1)
print(f"{id(l1) = }, {type(l1) = }")
print(f"{id(l1B) = }, {type(l1B) = }")

for ele in lst:
    l1B.append(ele)

print(f"{l1B = }")
print(f"{l1 = }")


print(f"{id(l3) = }, {type(l3) = }")
l3 = 10
print(f"{id(l3) = }, {type(l3) = }")
l7: int
l7 = "One"
print(f"{type(l7) = }")
print(f"{id(l7) = }, {type(l7) = }")


s1 = "Test"
s2 = "String"
s3 = s1

print(f"{id(s1) = }, {type(s1) = }")
print(f"{id(s3) = }, {type(s3) = }")


for c in s2:
    s3 += c

print(f"{id(s1) = }, {type(s1) = }, {s1 = }")
print(f"{id(s3) = }, {type(s3) = }, {s3 = }")


l6 = ['a', 'b', 'c', [1, 2, 3, 4, 5]]
print(l6)

l8 = l6             # Just a new reference to the existing object
l8 = l6[:]          # New list object is created, with the same contents as that of 'l6'
l8 = list(l6)       # New list object is created, with the same contents as that of 'l6'
l8 = l6.copy()      # Shallow copy

print(f"{l6 = }", f"{l8 = }", sep="\n")
print(f"{id(l6) = }", f"{id(l8) = }", sep="\n")

print(f"{l8[3] = }")
print(f"{l8[3][2] = }")
l8[3][2] = 33
print(f"{l8 = }")
print(f"{l6 = }")

print(f"{id(l6) = }")
print(f"{id(l8) = }")
print(f"{id(l6[1]) = }")
print(f"{id(l8[1]) = }")
l8[1] = "B"
print(f"{id(l6[1]) = }")
print(f"{id(l8[1]) = }")


print(f"{l8 = }")
print(f"{l6 = }")

print("="*50, "\n")

########################################################################


# This time let's do DEEP Copying
import copy

l6 = ['a', 'b', 'c', [1, 2, 3, 4, 5]]
l8 = copy.copy(l6)          # Shallow copy


l6 = ['a', 'b', 'c', [1, 2, 3, 4, 5]]
l8 = copy.deepcopy(l6)      # Deep copy

print(f"{l6 = }", f"{l8 = }", sep="\n")
print(f"{id(l6) = }", f"{id(l8) = }", sep="\n")

print(f"{l8[3] = }")
print(f"{l8[3][2] = }")
l8[3][2] = 33
print(f"{l8 = }")
print(f"{l6 = }")

print(f"{id(l6) = }")
print(f"{id(l8) = }")
print(f"{id(l6[1]) = }")
print(f"{id(l8[1]) = }")
l8[1] = "B"
print(f"{id(l6[1]) = }")
print(f"{id(l8[1]) = }")


print(f"{l8 = }")
print(f"{l6 = }")
