def Logger(fn):
    def wrapper(*vargs, **kwArgs):
        print(f"Calling {fn.__name__}...")
        ret_val = fn(*vargs, **kwArgs)
        print(f"Returning from {fn.__name__}...")
        return ret_val
    return wrapper

@Logger
def SayHello():
    print("Hello there!")

@Logger
def SayHi():
    print("Hi there")

@Logger
def add(a, b):
    return a+b

# fn = SayHello

# def wrapper():
#     print("Calling SayHello...")
#     fn()
#     print("Returning from SayHello...")

# SayHello = wrapper




# SayHello = Logger(SayHello)


#-- Consumer Code -----------------------

SayHello()
# wrapper()


# Calling SayHello...
# Hello there!
# Returning from SayHello

SayHi()


print(add(1, 2))