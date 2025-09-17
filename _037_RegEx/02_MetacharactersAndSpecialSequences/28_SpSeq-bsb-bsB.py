# \b - Word boundary; Matches the empty strings bordering the word.

# \B - Opposite of \b; Matches the empty strings not bordering the word

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Find words with 10 or more characters
result = re.findall(r"\b\w{10,}\b", string)
print(result, "\n")

# Using word boundary ensures that a substring is not picked up
result = re.findall(r"Euro", string)        # without word boundary
print(result, "\n")

result = re.findall(r"\bEuro\b", string)    # with word boundary
print(result, "\n")



# Check if the word 'cross' is part of the string, but not at the beginning of the string
result = re.findall(r"\Bcross", string)     # word shouldn't start with 'cross'
print(result, "\n")

result = re.findall(r"cross\B", string)     # word shouldn't end with 'cross'
print(result, "\n")

result = re.findall(r"\Bcross\B", string)   # word shouldn't start or end with 'cross'
print(result, "\n")