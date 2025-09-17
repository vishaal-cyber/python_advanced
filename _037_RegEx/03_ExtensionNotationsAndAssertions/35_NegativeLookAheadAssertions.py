# "{trgt-pattern}(?!{chk-pattern})"
# Returns a match with 'trgt-pattern' only if it is NOT followed by 'chk-pattern'

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Find the digits that are NOT followed by 
#       another digit greater than or equal to 5
#       OR a non-digit
result = re.findall(r"\d(?![5-9]|\D)", string)
print(result, "\n")

# All the words that are NOT followed by a whitespace character
result = re.findall(r"\b\w+\b(?!\s)", string)
print(result, "\n")