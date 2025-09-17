# Compile - Compiles a regex pattern into a regex object, which can be used 
#           for matching and searching, by methods like 'match' or 'search'.

# '\d' - Matches any decimal digit; this is equivalent to the set class [0-9]

import re

s = r"\d{3}"
print("s ->", type(s))

t = re.compile(s)
print("t [" + str(t) + "] ->", type(t))

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

result = re.findall(t, string) 
# findall() returns a list of all matches
print("t.findall(string) ->", result) 


result = re.findall(s, string)  
print("t.findall(string) ->", result)
