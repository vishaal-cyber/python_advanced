import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe \
    including the FTSE, fell by 11.48% – the worst day since it launched in 1998. \
    The panic selling prompted by the coronavirus has wiped £2.7tn off the value \
    of STOXX 600 shares since its all-time peak on 19 February."

# SYNTAX -> re.search(pattern, string, flags)
result = re.search(r'\d{3}', string)


print("type(result) ->", type(result))
print("result ->", result)

if result is not None:
    print("result.span() ->", result.span())
    print("result.start() ->", result.start())
    print("result.end() ->", result.end())
    print("Matched string", string[result.start():result.end()])
