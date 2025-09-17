# \d - any digit from 0-9

# \D - any non-digit character

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


result = re.findall(r"(\d)[a-z]", string)
print(result, "\n")
print()


# Find non-digit bordered by non-alphanumeric characters
result = re.findall(r"\W\D\W", string)
print(result, "\n")
result = re.findall(r"\W(\D)\W", string)
print(result, "\n")


