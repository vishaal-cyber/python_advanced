import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


result = re.findall(r"[0-9]", string)
print(result, "\n")

result = re.findall(r"[a-zA-Z]", string)
print(result, "\n")

result = re.findall(r"[^0-9]", string)
print(result, "\n")



# Whitespace characters
#   space
#   line-feed/newline (\n)
#   tab (\t)
#   vertical tab (\v)
#   form feed (\f)
#   carriage return (\r)

result = re.findall(r"[ \n\t\v\f\r]", string)
print("No. of matches:", len(result))
print(result, "\n")

print("No. of spaces in string:", string.count(' '))


# Opposite
result = re.findall(r"[^ \n\t\v\f\r]", string)
print("No. of matches:", len(result))
print(result, "\n")


# Filter Alphanumeric - 
#                   upper and lower case alphabets
#                   digits
#                   underscore
result = re.findall(r"[a-zA-Z0-9_]", string)
print("No. of matches:", len(result))
print(result, "\n")

# Opposite
result = re.findall(r"[^a-zA-Z0-9_]", string)
print("No. of matches:", len(result))
print(result, "\n")
