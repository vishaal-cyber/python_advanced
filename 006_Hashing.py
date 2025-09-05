## Hash (digest, hash-table)

# data  --Convert---> hash  (Unidirectional)

def hash1(num):
    return num%10

print(hash1(78))
print(hash1(36))
print(hash1(17))
print(hash1(87))


print(hash("Test"))

print(hash(15))
print(hash(1547))
print(hash(3781547))
# print(hash([1, 2, 3, 4, 5]))      # Unhashable

# 1. Only Keys can be hashed
# 2. Keys are immutable
# 3. Ergo, only immutables can be hashed

