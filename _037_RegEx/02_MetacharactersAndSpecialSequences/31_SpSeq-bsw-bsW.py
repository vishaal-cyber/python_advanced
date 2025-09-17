# \w -  any alphanumeric character, also called the word characters
#       includes the lower and upper case letters, digits, and underscore   

# \W -  

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998.\
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."


# Find words with 3 to 5 alphanumeric characters, surrounded by whitespaces
result = re.findall(r"\s(\w{3,5})\s", string)
print("Count -", len(result))
print(result, "\n")

# Find all non-alphanumeric characters
result = re.findall(r"\W", string)
print("Count -", len(result))
print(result, "\n")
