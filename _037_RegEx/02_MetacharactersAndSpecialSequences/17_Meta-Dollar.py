# $ - Matches only at the end of the line.

import re

# NEWLINE USED BELOW

string = '''The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February.'''

# Note that above string is modified version of earlier ones
# Triple quotes are used and a newline is introduced after "1998."

result = re.findall(r"\s(\w{2,})\W$", string, re.M)


print(result)