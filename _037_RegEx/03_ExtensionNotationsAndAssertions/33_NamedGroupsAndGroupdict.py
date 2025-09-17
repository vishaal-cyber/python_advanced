# (?P<{name}>{pattern}) - This is a named group.
# (?P=name) - This is a backreference to a previously named group

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result.groups())
print(result.group(1))
print(result.group(2))
print(result.group(3))
print("\n")


# Named Groups
result = re.search(r".+(?P<wordex>\b.+ex\b).+(?P<uppercase>\b[A-Z]{4}\b).+(?P<date>\d\d\s.+)\.", string)
print(result.groups())
print("\nIndexed Groups----")
print(result.group(1))
print(result.group(2))
print(result.group(3))

print("\nNamed Groups----")
print(result.group("wordex"))
print(result.group("uppercase"))
print(result.group("date"))

print("\nGroupdict---")
print("Dictionary\n", result.groupdict())
print("Wordex\n", result.groupdict()["wordex"])
print("Uppercase\n", result.groupdict()["uppercase"])
print("Date\n", result.groupdict()["date"])

print("\nBack reference to a named group ---")
ptrn = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b') # Identify word duplications
result = ptrn.findall('Paris in the the spring time time')
print(result)