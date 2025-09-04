#!/usr/bin/env py

# name = input("Please enter your name: ")
# print("Hello", name)

def isOdd1(num):
    return num%2 == 1

def isOdd2(num):
    return num%2 != 0

fl = float("-3")
remaining = fl%2
print(type(remaining), remaining)

print(isOdd1(fl))
print(isOdd2(fl))

from decimal import Decimal

dc = float("-3")
remaining = dc%2
print(type(remaining), remaining)

print(isOdd1(dc))
print(isOdd2(dc))
