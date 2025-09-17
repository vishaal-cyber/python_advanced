# \A -  Matches at the beginning of the string.
#       If the string is not multiline, then it behaves like the ^ character.
#       If string is multiline, \A (unlike the ^) still matches at the beginning 
#       of the string only, and not at the beginning of each line, while the ^ matches 
#       at the beginning of each line in multiline string i.e. after each newline character.

# \Z -  Matches at the end of the string
#       If the string is not multiline, then it behaves like the $ character.
#       If string is multiline, \Z (unlike the $) still matches at the end of the string 
#       only, and not at the end of each line, while the $ matches at the end of each line 
#       in multiline string i.e. before each newline and the end of the string.


import re

# NEWLINE USED BELOW

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\n\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

# Using the ^
# result = re.findall(r"^([A-Z].*?)\s", string, re.M)   # returns a list of strings
result = re.finditer(r"^([A-Z].*?)\s", string, re.M)    # returns a list of match-objects
for x in result:
    print(x.group(), x.span())
print()

# Using the \A
result = re.finditer(r"\A([A-Z].*?)\s", string, re.M)
for x in result:
    print(x.group(), x.span())
print()



# Using the $
result = re.findall(r"\W$", string, re.M)
print(result, "\n")

result = re.finditer(r"(\w+)\W$", string, re.M)
for x in result:
    print(x.group(), x.span())
print()

# Using the \Z
result = re.findall(r"\W\Z", string, re.M)
print(result, "\n")

result = re.finditer(r"(\w+)\W\Z", string, re.M)
for x in result:
    print(x.group(), x.span())
print()