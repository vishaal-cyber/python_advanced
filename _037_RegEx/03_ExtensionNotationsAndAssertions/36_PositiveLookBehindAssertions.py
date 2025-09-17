# "(?<={chk-pattern}){trgt-pattern}"
# Returns a match with 'trg-pattern' only if it IS preceded by 'chk-pattern' (lookbehind pattern)

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

# Find all numbers preceded by a space
result = re.findall(r"(?<=\s)\d{1,}", string)
print(result, "\n")

# All the words that are preceded by a comma and a whitespace together
result = re.findall(r"(?<=,\s)\b\w+\b", string)
print(result, "\n")