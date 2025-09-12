class Parent:
    def __init__(self):
        print("Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class")

class GrandChild(Child):
    def __init__(self):
        super().__init__()
        print("Grandchild class")

class OtherParent:
    def __init__(self):
        print("Other Parent class")

class MultipleChild(OtherParent, Parent):
    def __init__(self):
        super(OtherParent, self).__init__()
        print("Multiple Child class")

class Sibling(OtherParent):
    def __init__(self):
        super().__init__()
        print("Sibling class")

class Cousin(OtherParent, Parent):
    def __init__(self):
        super(Parent, self).__init__()
        print("Cousin class")

class CoopParent:
    def __init__(self):
        print("Coop Parent class")

class CoopChild1(CoopParent):
    def __init__(self):
        super().__init__()
        print("Coop Child 1 class")

class CoopChild2(CoopParent):
    def __init__(self):
        super().__init__()
        print("Coop Child 2 class")

class CoopGrandchild(CoopChild1, CoopChild2):
    def __init__(self):
        super().__init__()
        print("Coop Grandchild class")

def main():
    gc = GrandChild(); print("\n")      # Output: Parent class, Child class, Grandchild class
    mc = MultipleChild(); print("\n")   # Output: Other Parent class, Parent class, Multiple Child class
    s = Sibling(); print("\n")          # Output: Other Parent class, Sibling class
    c = Cousin(); print("\n")           # Output: Other Parent class, Parent class, Cousin class
    cg = CoopGrandchild(); print("\n")  # Output: Coop Parent class, Coop Child 1 class, Coop Child 2 class, Coop Grandchild class

if __name__ == '__main__':
    main()