class SimpleList:
    def __init__(self, items = []):
        print("SimpleList.__init__()")
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]
    
    def sort(self):
        self.items.sort()

    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return f"{type(self).__name__} ({self.items!r})"

#---------------------------------------------------------------------------------

class SortedList(SimpleList):
    def __init__(self, items=[]):
        print("SortedList.__init__()")
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

#---------------------------------------------------------------------------------

class IntList(SimpleList):
    def __init__(self, items=[]):
        print("IntList.__init__()")
        for x in items:
            self.validate(int(x))
        super().__init__([int(x) for x in items])

    @staticmethod
    def validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList supports only integer values.")
        
    def add(self, item):
        self.validate(int(item))
        super().add(int(item))

#---------------------------------------------------------------------------------

# class SortedIntList(IntList, SortedList):
class SortedIntList(SortedList, IntList):
    pass

#---------------------------------------------------------------------------------

def Test1():
    lst1 = SimpleList()
    print(lst1)

    lst2 = SimpleList((1, 2, 3, 4, 5, 6))
    print(lst2)

    lst2.add(72)
    lst2.add(61)
    print(lst2)

def Test2():
    s1 = SortedList([4, 3, 78, 1])
    print(s1)
    print(len(s1))
    s1.add(-35)
    print(s1)

def Test3():
    il = IntList((1, 2, '3', 4))
    il.add(9)
    il.add(7)
    il.add('5')
    print(il)

def Test4():
    try:
        sil = SortedIntList([42, 23, 3])
        sil.add(-1234)
        print(sil)
    except Exception as ex:
        print(f"{ex!r}")

    print("\n")

    try:
        sil2 = SortedIntList([5, 2, 8, '4', 7, 3])
        print(sil2)
    except Exception as ex:
        print(f"{ex!r}")

    print("\n")

    try:
        sil3 = SortedIntList([5, 2, 8, 'four', 7, 3])
        print(sil3)
    except Exception as ex:
        print(f"{ex!r}")

    print("\n")



if __name__ == "__main__":
    # Test1()
    # Test2()
    # Test3()
    Test4()
