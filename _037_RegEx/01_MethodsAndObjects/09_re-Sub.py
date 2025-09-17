# 'sub' - Used to replace one or more occurances of a pattern with a different string.

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

print()
# SYNTAX -> result = re.sub(patter, repl, string, count, flags)
result = re.sub(r"[A-Z]{2,}", "INDEX", string)
print("type(result) ->", type(result))
print("result ->", result)

print()
result = re.sub(r"[A-Z]{2,}", "INDEX", string, 2)
print("type(result) ->", type(result))
print("result ->", result)
