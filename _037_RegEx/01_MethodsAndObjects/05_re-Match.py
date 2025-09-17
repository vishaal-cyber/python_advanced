# 'match' - returns a match only if the match is at the beginning of the string.
#           else return 'None'.

# '\w' - matches any alphanumeric (lower or upper case) and underscore.
#      - doesn't match whitespaces
# '\W' - matches any non-alphabet.
# '\d' - matches any digit.
# '\D' - matches any non-digit.
# '\s' - matches any whitespace.
# '\S' - matches any non-whitespace.
# '\b' - matches the empty string at the beginning or end of a word.
# '\B' - matches the empty string not at the beginning or end of a word.
# '\Z' - matches the empty string at the end of a string.
# '\A' - matches the empty string at the beginning 

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

result = re.match(r'\w{3}', string)
print("result ->", result)

result = re.match(r'\w{4}', string)
print("result ->", result)
