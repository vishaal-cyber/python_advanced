# 'findall' - Returns a list containing all matches, 
#             unlike 'match' which returns the first match only.
#             Return empty list if no matches are found.
# 'finditer' - Returns an iterator yielding match objects

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

result = re.findall(r'\d{3}', string)
print("type(result) ->", type(result))
print("result ->", result)

print("\n")
result = re.findall(r'\d{5}', string)
print("type(result) ->", type(result))
print("result ->", result)

