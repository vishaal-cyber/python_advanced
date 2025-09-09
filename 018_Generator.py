def SimpleGeneratorFunc():
    print("About to yield 1...")
    yield 1
    print("About to yield 2...")
    yield 2
    print("About to yield 3...")
    yield 3


for x in SimpleGeneratorFunc():
    print(x, end=' ')
print()


gen = SimpleGeneratorFunc()
print(f"{type(gen) = }")



# res = next(gen)
# print(res)
# res = next(gen)
# print(res)
# res = next(gen)
# print(res)
# res = next(gen)
# print(res)


while True:
    try:
        res = next(gen)
        print(res)
    except StopIteration:
        print("Done with the generation!!")
        break


###################################################
## Fibonacci Generator

def FibGen(n):
    """Generates a sequence of 'n' Fibonacci numbers"""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

gen = FibGen(10)
# gen.__next__()
# gen.__iter__()

# lst = []
# lst.__iter__()

while True:
    try:
        res = next(gen) #  gen.__next__()
        print(res)
    except StopIteration:
        print("Done with the generation!!")
        break

# Iterable supports __iter__() method
# Iterator supports __iter__() and __next__(), both
# Generator mimicks the Iterator


# lst = []
# itr = lst.__iter__()
# print(f"{type(itr) = }")

# for x in lst: # iter(lst) --> gets the iterator for list
#     print(x)


# # gen = SimpleGeneratorFunc()
# for x in SimpleGeneratorFunc(): # iter(SimpleGeneratorFunc())  ---> iter(gen)  --> gen.__iter__() --> itr {of type iterator}
#     print(x)

