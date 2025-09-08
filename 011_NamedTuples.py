stud1 = {
    'name': 'Pravin',
    'age': 14,
    'standard': 8
}

print(stud1)

print(stud1["name"])

## Named Tuple #######################

from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'standard'])
s1 = Student("Abhijeet", 16, 10)
s2 = Student("Manish", 12, 6)

print(s1)
print(s1.name)


p1 = {
    'x': 10,
    'y': 20
}


# Point = namedtuple("Point", ['x', 'y'])
Point = namedtuple("Point", 'x y')
p2 = Point(10, 20)
print(p2.x, p2.y)