# Conditional Construct
# num  = 40

# if num > 20:
#     print("Greater")
# elif num < 20:
#     print("Lesser")
# else:
#     print("Twnenty")

# print("Done")

# Match Condition
# match num:
#     case 10:
#         print("Ten")
#     case 20:
#         print("Twenty")
#     case 30:
#         print("Thirty")
#     case _:
#         print("Other number")

# def Ten():
#     print("Ten")

# def Twenty():
#     print("Twenty")

# def Thirty():
#     print("Thirty")

    
# num = 20
# match num:
#     case 10:
#         Ten(); Twenty(); Thirty()
#     case 20:
#         Twenty(); Thirty()
#     case 30:
#         Thrity()
#     case _:
#         print("Other number")


## Loops ###########################################################

## While Loop ; NO do-while loops
num = 0

while num < 5:
    print(num)
    num += 1

lst1 = [1, 2, 3, 4, 5]
ln = len(lst1)

idx = 0

val = 7
while idx < ln:
    if val == lst1[idx]:
        print("Found the number", val," at the index", idx)
        break
    idx += 1
else:
    print("Number was not found!")


# if idx == ln:
#     print("Number was not found!")


## For --> (init;  cond;   step)

for val in lst1:
    print(val, end=" - ")
print()

# for i in [1, 2, 3, 4, 5]:
for i in range(1, 11, 2):
    print("Hi", i)

for _ in range(5):
    print("Hello")


val = 7 #;  x = 20
for x in lst1:
    if val == x:
        print("Found the number", val," at the index", idx)
        break
else:
    print("Number not found")



print("\n", "="*25, "\n")

val = 7
# for idx in range(len(lst1)):
for idx in range(0, len(lst1), 1):
    if val == lst1[idx]:
        print("Found the number", val," at the index", idx)
        break
else:
    print("Number not found")

for i in range(20):
    if (i%2 != 0):
        continue
    print(i, end=" - ")
print()


def Forty():
    pass

for _ in range(5):
    pass

print("Test")

def default():
    print("default")

# int add(int a, int b)
# {}

# if(i < 10)
#     printf("Lesser")
#     printf("Continuing...")

x = 20
if ((val == 10) and (x == 20)):
    print("Test")
