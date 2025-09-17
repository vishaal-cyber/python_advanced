# {} - repetition operator for the preceeding expression in regex patterns

import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

result = re.findall(r"\b\w{4}\b", string)
# \w - any word character (a-z, A-Z, 0-9, _)
# \b - word boundary
print(result, "\n")


# Find all words that are 
#       at least 3 chars long
#       no more than 5 chars long
result = re.findall(r"\b\w{3,5}\b", string)
print(result, "\n")


# Find all words that are 
#       at least 3 chars long
#       no upper limit
result = re.findall(r"\b\w{3,}\b", string)
print(result, "\n")


# Find the first set of 3-6 digits
number = "12391827172820919011001911"
result = re.search(r"\d{3,6}", number)
print(result, "\n")

# Non-Greedy behaviour
result = re.search(r"\d{3,6}?", number)
print(result, "\n")
