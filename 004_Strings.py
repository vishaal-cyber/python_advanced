s1 = "Test"
s2 = 'String'

s3 = "This is Abhijeet's notebook"
s4 = 'He said, "Thanks"'

print(s1, s2, s3, s4, sep="\n")

s5 = '''Help String
Invalid usage of method
Correct usage specified as below
-n : no. of lines
-d : detach'''

print(s5)

s6 = "This is \
is on \
different \
lines"

print(s6)

s7 = """This is
a 
multiline 
comment"""

print(s7)


s8 = "Fisrt""Second"
print(s8)


## Escaape Sequence
## Format Strings
## Slicing

path = r"c:\Users\ramakant\new_folder\textpad.txt"
print(path)

# printf("%d is te count of %s type of items", count, category)

s1 = "We are in a %s training for %d days"
print(s1%('Python', 12))

s1 = "We are in a {} training for {} days"
print(s1.format('Python', 12))

tech = 'Python'
duration = 12
print(f"We are in a {tech} training for {duration} days")

print("tech =", tech)
print(f"{tech = }")


## String Slicing
s2 = f"We are in a {tech} training for {duration} days"
print(s2)

for idx in range(3, 6, 1):
    print(s2[idx], end='')
print()

print(s2[3:6])
print(s2[3:])
print(s2[:6])

print(s2[len(s2) - 1])
print(s2[-1])
print(s2[-4:])

print(s2[-11:-5])


# We are in a Python training for 12 days
# days We are --> s2[-5:6], s2[-4:6], s2[-4:]+s2[:6]
print("="*25)
print(s2[-4:6])
print(s2[-4:]+s2[:6])



s3 = "0123456789"


# s3[start : stop : step]
print(s3[::2])
print(s3[1::2])
print(s3[::-1])
print(s2[-13:-21:-1])

print("="*25)
print(s2[3:9:-1])
print(s2[19:27:1])
print(s2[26:18:-1])
