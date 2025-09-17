# "(?<!{chk-pattern}){trgt-pattern}"
# Returns a match with 'trg-pattern' only if it is NOT preceded by 'chk-pattern' (lookbehind pattern)

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Find any set of consequetive digits that are NOT preceded by whitespace
result = re.findall(r"(?<!\s)\d{1,}", string)
print(result, "\n")

# Find all occurences of the letter 'x' (case insensitive) 
# that are NEITHER preceded NOR followed by another letter 'x'
result = re.findall(r"(?<!x)x(?!x)", string, re.I)
print(result, "\n")