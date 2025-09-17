# ^ - Matches only at the beginning of the line.

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

# Search for a 3 letter word at the beginning of the line.
result = re.search(r"^\w{3}", string) 
print(result)

print()
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
\nThe panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."
print(string + "\n")

result = re.findall(r"^\w{3}", string) 
print(result, "\n")

result = re.findall(r"^\w{3}", string, re.M)
print(result, "\n")
