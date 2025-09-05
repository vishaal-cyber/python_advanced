# Set - Mutable collection of 'keys' (i.e. immutables)
# Key - Hashable object
# Hashable - Non-mutating; Immutable

# s1 = {1, 2, 3, 4, 5}
# s2 = {}                 # defaults to a dict type
# s3 = set()
# s4 = set([10, 20, 30, 40])

# print(f"{type(s1) = }, {s1 = }")
# print(f"{type(s2) = }, {s2 = }")
# print(f"{type(s3) = }, {s3 = }")
# print(f"{type(s4) = }, {s4 = }")

# l1 = [1, 2, 3, 4]

# s5 = {1, 2, 3}
# s5.add(5)
# print(s5)
# # s5.add(l1)
# s5.update(l1)
# print(s5)


# s5.remove(3)
# print(s5)

# # s5.remove(3)
# s5.discard(3)
# s5.discard(5)
# print(s5)

# s5.add(2)
# print(s5)

# s6 = {"One", "Two", "Three", "Four"}

# for val in s6:
#     print(val)
#     if val == "Two":
#         print(id(val))


# for val in s6:
#     print(val)
#     if val == "Two":
#         print(id(val))

# s6.add("Two")

# for val in s6:
#     print(val)
#     if val == "Two":
#         print(id(val))

# print("Two" in s6)

# print(s6.pop())
# print(s6)

#####################################################

# s1 = {'a', 'b', 'c', 'd'}
# s2 = {'c', 'd', 'e', 'f'}

# print(s1 & s2); print(s1.intersection(s2))
# print(s1 | s2); print(s1.union(s2))
# print(s1 - s2); print(s1.difference(s2))
# print(s1 ^ s2); print(s1.symmetric_difference(s2))

# s3 = s1 & s2
# print(s3 <= s1, end=" "); print(s3.issubset(s1))
# print(s1 >= s3, end=" "); print(s1.issuperset(s3))

# s4 = {'p', 'q', 'r'}
# print(s1 & s3 == set(), end=" "); print(s1.isdisjoint(s3))
# print(s1 & s4 == set(), end=" "); print(s1.isdisjoint(s4))


########################################################


l1 = [1, 2 , 3, 4]
l2 = [1, 2, 3, l1]
l3 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

print(l3[1][2])
print(l3)

# s1 = {
#     {1, 2, 3},
#     {4, 5, 6},
#     {7, 8, 9}
# }
# print(s1)


# regions = {"India", "Russia", "USA", "China"}
# loading = {"automated_loading", "manual_loading"}
# env_controlled = {"plain", "ac", "temp_controlled"}

# categories = {regions, loading, env_controlled}

# print(categories)


## Frozenset
regions = frozenset({"India", "Russia", "USA", "China"})
loading = frozenset({"automated_loading", "manual_loading"})
env_controlled = frozenset({"plain", "ac", "temp_controlled"})

categories = {regions, loading, env_controlled}

for bunch in categories:
    for key in bunch:
        print(key, end=", ")
    print()


print(categories)
