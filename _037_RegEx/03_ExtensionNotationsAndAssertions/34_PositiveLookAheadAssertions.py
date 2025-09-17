# "{trgt-pattern}(?={chk-pattern})"
# Returns a match with 'trgt-pattern' only if it IS followed by 'chk-pattern'

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Find a 5 lettered (uppercase) word followed by a 3 digits
result = re.findall(r"[A-Z]{5}\s(?=[0-9]{3})", string)
print(result, "\n")   # result includes the spaces

# Remove the space from the results by using groups
result = re.findall(r"([A-Z]{5})\s(?=[0-9]{3})", string)
print(result, "\n")

# Find occurances of "Euro", 
# such that they are followed by at least one lowercase letter
result = re.findall(r"Euro", string)
print("Without assertion =>", result)

result = re.findall(r"Euro(?=[a-z]+)", string)
print("With assertion =>", result, "\n")
