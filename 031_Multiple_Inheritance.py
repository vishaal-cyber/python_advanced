class SimpleList:
    def __init__(self, items = []):
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
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

#---------------------------------------------------------------------------------

class IntList(SimpleList):
    def __init__(self, items=[]):
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

if __name__ == "__main__":
    # Test1()
    # Test2()
    Test3()
