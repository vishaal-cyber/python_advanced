# re.I - IGNORECASE
# re.M - MULTILINE
# re.S - DOTALL
# re.X - VERBOSE
# flags = re.I | re.M | re.S | re.X

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

string2 = '''The string is a 
multiline comment 
for testing 
the behaviour 
of the method.
The test results will 
be based on 
these characters here.'''


# IGNORECASE ############################
print("\nIGNORECASE ##############")
result = re.findall(r"the", string)
print("result ->", result)

print()
result = re.findall(r"the", string, re.I)
print("result ->", result)

# MULTILINE ############################
print("\nMULTILINE ###############")
result = re.findall(r"^The", string2)
print("result ->", result)

print()
result = re.findall(r"^The", string2, re.M)
print("result ->", result)

print()
result = re.findall(r"^The", string2, re.M|re.I)
print("result ->", result)

# DOTALL ############################
print("\nDOTALL ###################")
result = re.findall(r".+", string2) # '.+' -> all chars except newline
print("len(result) ->", len(result))
print("result ->", result)

print()
result = re.findall(r".+", string2, re.S)
print("len(result) ->", len(result))
print("result ->", result)

string3 = "Hello\nPython"
print()
result = re.search(r".+", string3)  # '.+' -> all chars except newline
print("result ->", result)

print()
result = re.search(r".+", string3, re.S)
print("result ->", result)

# VERBOSE #############################
print("\nVERBOSE ####################")
print()

# result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
# Can be rewritten as below
result = re.search(r'''.+\s     #Beginning of the string
                   (.+ex)       #Searching for index
                   .+           #Middle of the string
                   (\d\d\s.+).  #Date at the end''', string, re.X)

# 're.X' -> Enable verbose REs, which can be organized more cleanly and understandably.
# When this flag has been specified, whitespace within the RE string is ignored, 
# except when the whitespace is in a character class or preceded by an unescaped 
# backslash; this lets you organize and indent the RE more clearly. 
# This flag also lets you put comments within a RE that will be ignored by the engine; 
# comments are marked by a '#' that’s neither in a character class or preceded by 
# an unescaped backslash.

print("result.groups() ->", result.groups())





