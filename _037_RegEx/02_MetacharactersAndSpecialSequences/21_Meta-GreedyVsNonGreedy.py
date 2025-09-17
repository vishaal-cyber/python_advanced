# Non-Greedy
# Adding a question mark (?) after the asterisk, plus-sign or question mark
# turns off the greedy behaviour
#   *?
#   +?
#   ??

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Modifying the '*' behaviour
result = re.findall(r"\d\d\d*", string)
print(result, "\n")

result = re.findall(r"\d\d\d*?", string)
print(result, "\n")
print()

# Modifying the '+' behaviour
result = re.findall(r"\d\d\d+", string)
print(result, "\n")

result = re.findall(r"\d\d\d+?", string)
print(result, "\n")
print()

result = re.findall(r"E.* ", string)
print(result, "\n")

result = re.findall(r"E.*? ", string)
print(result, "\n")
print()

result = re.findall(r"E.+ ", string)
print(result, "\n")

result = re.findall(r"E.+? ", string)
print(result, "\n")
print()

# Modifying the '?' behaviour
result = re.findall(r"\d\d\d?", string)
print(result, "\n")

result = re.findall(r"\d\d\d??", string)
print(result, "\n")
print()

