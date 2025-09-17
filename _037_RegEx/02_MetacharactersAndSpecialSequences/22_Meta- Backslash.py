# \ - can have either of the two roles:
# 1. Special Sequence - \A, \b, \B, \d, \D, \s, \S, \w, \W, etc.
# 2. Escape character - Escaping and matching a symbol that would 
#                       otherwise be interpreted as a special sequence
#                       or a character c  viz.  \. \? \[ \] \( \) \^ \$ \{ \} 


import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

# Special Sequence
result = re.findall(r"\d", string)
print(result)


# Escaping symbols with special meaning
result = re.findall(r"\.", string)
print(result)
