def PrintCollection(data):
    # for val in data:
    #     print(val, end="--")
    # print()

    print(f"{type(data)}")
    while data:
        print(data.pop(), end='--')
    print()


def Caller():
    lst1 = (1, 2, 3, 4, 5)
    # PrintCollection(lst1.copy())  # No 'copy' method in tuple
    # print(lst1[:])
    PrintCollection(lst1[:])

    print("\n\nCollection --> [", end='')
    for val in lst1:
        print(val, end=', ')
    print("]")


# Caller()


def Test1():
    lst1 = []
    st1 = set()

    lst1.append(4)
    lst1.append(5)
    lst1.append(1)
    lst1.append(2)
    lst1.append(3)


    st1.add(4)
    st1.add(5)
    st1.add(1)
    st1.add(2)
    st1.add(3)

    print(lst1)
    print(st1)

    # lst1[0]
    # st1[1]

Test1()