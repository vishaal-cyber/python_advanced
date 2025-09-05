# Dictionary: Unordered collection of key:value pairs
# Key: hashable
# Value: Any

l1 = [1, 2, 3, 4, 5]

d1 = {}
d2 = {'Manish': 85, 'Abhijeet': 75, 'Pravin':92, 'Rakesh': 98}
d3 = dict()
d4 = dict(A=90, B=80, C=70, D=60)
d5 = dict().fromkeys(l1)

print(f"{type(d1) = }, {d1 = }")
print(f"{type(d2) = }, {d2 = }")
print(f"{type(d3) = }, {d3 = }")
print(f"{type(d4) = }, {d4 = }")
print(f"{type(d5) = }, {d5 = }")

print(len(d2))
print(len(d5))

print(d4['A'])
print(d5[1])
d5[1] = 10
print(d5)
d5[6] = 60
print(d5)

if 5 in d5:
    d5[5] = 50

if 7 in d5:
    d5[7] = 70

print(d5)

print(d5[6])

if 8 in d5:
    print(d5[8])

print(d5.get(8))
print(d5.get(2))

print(d5)

k = 8
if k not in d5:
    d5[k] = k*10

print(d5)

print(d5.pop(5))
print(d5)

print(d5.popitem())
print(d5)

l2 = list(d5)
print(l2)

l3 = list(d5.keys())
print(l3)

l4 = list(d5.values())
print(l4)

l5 = list(d5.items())
print(l5)

for x in d5:
    print(x, end=" ")
print()

for x in d5.keys():
    print(x, end=" ")
print()

for x in d5.values():
    print(x, end=" ")
print()

for x in d5.items():
    print(x, end=" ")
print()

for k, v in d5.items():
    print(f"{k} --> {v}")
print()


d5.update(d2)
print(d5)

d7 = {'Manish': 10, 'Abhijeet': 20, 'Pravin':30, 'Rakesh': 40}
d5.update(d7)
print(d5)
