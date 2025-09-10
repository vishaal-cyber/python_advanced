class Integer:
    def __init__(self, val):
        self.data = int(val)

    def __str__(self):
        return str(self.data)
    
    def __add__(self, other):
        if isinstance(other, int):
            res = self.data + other
        else:
            res = self.data + other.data
        return Integer(res)

def Test1():
    i1 = Integer(10)
    i2 = Integer(20)

    print(i1)
    print(i2)

    i3: Integer = i1 + i2
    # i1 + i2   --->   i1.__add__(i2)
    print(i3)

    i4 = i3 + 5     # i3.__add__(5)
    print(i4)

    i5 = 5 + i4     # Cannot be handled as   5.__add__(i4)
    print(i5)


if __name__ == "__main__":
    Test1()