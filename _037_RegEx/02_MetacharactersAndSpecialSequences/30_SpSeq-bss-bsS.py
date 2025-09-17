# \s -  any whitespace {space, tab, newline, return, formfeed, vertical tab}
#       [ \t\n\r\f\v]

# \S -  any non-whitespace character

import re

# NEWLINE USED BELOW

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\n\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


result = re.findall(r"\s", string)
print(result, "\n")

# Find all occurances of at least 8 consequetive non-whitespace characters
result = re.findall(r"\S{8,}", string)
print(result, "\n")
