class FibGen:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.count < self.num:
            x = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return x
        else:
            raise StopIteration


myFib = FibGen(10)
myIter = iter(myFib)
for x in myFib:           # 1. Creates an iterator from myFib {it = iter(myFib)}  2. Iterates using the iterator {next(it)}
    print(x, end=' ')
print()


num = []
sq = [x**2 for x in range(10000) ]

dt = {}
for k, v in dt.items():
    pass

for k in dt.keys():
    pass
for v in dt.values():
    pass
for k in dt:
    pass