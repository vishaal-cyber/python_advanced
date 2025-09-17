# 'fullmatch' - matches the entire string

# '.' - matches any character except the new line
# Using flags we can treat the newline as an acceptable character - Later discussion

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

print("len ->", len(string))

result = re.fullmatch(r'.{285}', string)
print("result ->", result)

result = re.fullmatch(r'\w{285}', string) # '\w' doesn't match whitespaces
print("result ->", result)
