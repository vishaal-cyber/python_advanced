# . - represents any character except a new line character. 
# [A-Z][a-z][0-9] $ # ? , : etc.

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r"(.+)", string) # Just validating that the target has no newlines.
print(result)

print(result.group(1))

if (string == result.group(1)):
    print("\nThere are indeed no newlines.")
else:
    print("\nThe target has newline(s) in it.")