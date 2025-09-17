# [] - A set of characters and character classes
# Quantifiers define quantities:
#   * - 0 or more
#   + - 1 or more
#   ? - 0 or 1


import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Look for occurances of w, x, k OR q in the string
result = re.findall(r"[wxkq]", string)
print(result, "\n")

print("\nPositions:-")
# Find positions of all occurances of a substring/pattern
positions = [m.span() for m in re.finditer(r"st", string, re.I)]
print(type(positions))
print('"st" ->', positions, "\n")

# Find positions of all occurances of characters from a char-class
positions = [m.start() for m in re.finditer(r"[wxkq]", string)]
print(type(positions))
print('"[wxkq]" ->', positions, "\n")

# Look for occurances of a, b, c OR d in the string
result = re.findall(r"[a-d]", string)
print(result, "\n")

# Look for occurances of characters S to W in the string
result = re.findall(r"[S-W]", string)
print(result, "\n")

# Look for occurances of digits 1 to 5 in the string
result = re.findall(r"[1-5]", string)
print(result, "\n")

# Look for two consecutive letters, first between a-f and second between c-w
result = re.findall(r"[a-f][c-w]", string)
print(result, "\n")
# O/P - All such combinations


# Look for two digits, first between 0-5 and second between 7-9
result = re.findall(r"[0-5][7-9]", string)
print(result, "\n")


# Look for combination of 1 digit and 1 letter
result = re.findall(r"[0-9][a-z]", string)
print(result, "\n")


# NEGATION - Use a caret inside the [], at the beginning
# Look for everything except X
result = re.findall(r"[^X]", string)
print(result, "\n")
print("Is X present in the result?", 'X' in result)
print()

# Special characters lose their special meaining, if inside the []
result = re.findall(r"(.+?)", string)
print(result, "\n")
result = re.findall(r"[(.+?)]", string)
print(result, "\n")
