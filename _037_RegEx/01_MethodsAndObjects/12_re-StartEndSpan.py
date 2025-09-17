import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
of STOXX 600 shares since its all-time peak on 19 February."

print()
result = re.search(r".+\s(.+ex).+(\d\d\s.+).", string)
print("result.group(1) ->", result.group(1))
print("result.group(2) ->", result.group(2))

print()
print("result.start(1), result.start(2)\n", result.start(1), result.start(2))
print("string.index('index'), string.index('19 February')\n", string.index('index'), string.index('19 February'))

print()
print("result.end(1), result.end(2)\n", result.end(1), result.end(2))
print("string.index('index'), string.index('19 February')\n", string.index('index') + len('index'), string.index('19 February') + len('19 February'))

print()
print("string[result.start(1): result.end(1)] ->", string[result.start(1): result.end(1)])
print("string[result.start(2): result.end(2)] ->", string[result.start(2): result.end(2)])


## Using span() ##
print()
print("result.span(1)\n", result.span(1))
print("string[result.span(1)[0]: result.span(1)[1]]\n", string[result.span(1)[0]: result.span(1)[1]])
print()
print("result.span(2)\n", result.span(2))
print("string[result.span(2)[0]: result.span(2)[1]]\n", string[result.span(2)[0]: result.span(2)[1]])
