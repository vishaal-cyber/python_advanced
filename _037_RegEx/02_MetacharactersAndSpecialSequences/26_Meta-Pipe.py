# A|B|C - Where A, B and C are distinct regular expressions, 
#         and the regular expression A|B|C matches either A, B or C.

# NOT Greedy as the Pipe achieves a single pattern match with any of A, B or C,
# NOT all of them.
# RegEx engine tries the patterns one at a time from left to right, 
# and stops at the first match. 
# Rest of the patterns are ignored.

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r"\d{3}|\d{4}|\b[A-Z]{4}\b", string)
print(result, "\n")

# Design the first pattern to fail
result = re.search(r"\d{8}|\d{4}|\b[A-Z]{4}\b", string)
print(result, "\n")
