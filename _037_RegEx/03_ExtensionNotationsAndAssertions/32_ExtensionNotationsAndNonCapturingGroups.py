# (?{extn}{expr}) - Extension notation; variety of extentions can be specified

# (?:{expr}) - ':' makes it a non capturing group

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result, "\n")
print(result.groups())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print("\n")


# Suppress group1 capture {non-capturing group}
result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result, "\n")
print(result.groups())
print(result.group(1))
print(result.group(2))
print("\n")