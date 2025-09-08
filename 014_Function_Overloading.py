## Function Overloading

# def add1(a, b):
#     return a+b

# def add2(a, b, c):
#     return a+b+c

# def add3(a, b, c, d):
#     return a+b+c+d




# def add(*vargs):                # <-- Pack all args into 'vargs'
#     match (len(vargs)):
#         case 2:
#             return add1(*vargs)        # <-- Unpack 'vargs' to get all distinct args 
#         case 3:
#             return add2(*vargs)        # <-- Unpack 'vargs' to get all distinct args 
#         case 4:
#             return add3(*vargs)        # <-- Unpack 'vargs' to get all distinct args 



# print(f"{type(add) = }")


#--Using Multiple Dispatch-----------------------------------------
from multipledispatch import dispatch


@dispatch(int, int)
def add(a, b):
    print("Adding integers")
    return a+b

@dispatch(str, str)
def add(a, b):
    print("Adding strings")
    return a+b

@dispatch(int, int, int)
def add(a, b, c):
    return a+b+c

@dispatch(int, int, int, float)
def add(a, b, c, d):
    return a+b+c+d

#--Consumer Code---------------------



print(add(1, 2, 3))
print(add(1, 2))
print(add(1, 2, 3, 4.0))
print(add("Test", "String"))
