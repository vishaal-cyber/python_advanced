#region Basic

# fruits = ['apple', 'banana', 'cherry', 'dragonfruit', 'kiwi', 'mango']
# bowl = []
# for x in fruits:
#     if 'a' in x:
#         bowl.append(x)
# print(bowl)


# nums = [1, 2, 3, 4, 5]
# sq = []
# for x in nums:
#     sq.append(x**2)
# print(sq)


# ## [ element-to-add         elem-from-collection      cond/trans]
# bowl2 = [x         for x in fruits      if 'a' in x]
# print(bowl2)

# sq2 = [x**2     for x in nums]
# print(sq2)

# print([x**2 for x in nums])


# print([x**2  for x in range(2, 21, 2)])

# print([x**2  for x in range(1, 21)   if x%2 == 0])



# obj = [x         for x in fruits      if 'a' in x]; print(f"{type(obj) = }; {obj = }")
# obj = {x         for x in fruits      if 'a' in x}; print(f"{type(obj) = }; {obj = }")
# obj = {x:len(x)  for x in fruits      if 'a' in x}; print(f"{type(obj) = }; {obj = }")
# obj = (x         for x in fruits      if 'a' in x); print(f"{type(obj) = }; {obj = }")      # NOT  a tuple, but a Generator obj
# obj = tuple(x    for x in fruits      if 'a' in x); print(f"{type(obj) = }; {obj = }")

#endregion

# print(help(dir))

obj = 10

# members = [member     for member in dir(obj)]
members = [member     for member in dir(obj)      if not member.startswith('_')]
print(members)
members = [member     for member in dir(obj)      if not member.startswith('_')  and callable(getattr(obj, member))]
print(members)


print(" 'str' public methods --> ", [member     for member in dir(str)      if not member.startswith('_')  and callable(getattr(str, member))])
