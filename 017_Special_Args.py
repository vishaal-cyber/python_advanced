# / - Anything to the left will always be positional args
# * - Anything to the right will always be keyworded args

def operation(a, b, /, c, d, *, e, f):
    pass


#--Consumer Code ---------------------------
# operation(1, 2, 3, 4, 5, 6)
# operation(a=1, b=2, c=3, d=4, e=5, f=6)
# operation(e=5, f=6, a=1, b=2, c=3, d=4)
operation(1, 2, c=3, d=4, e=5, f=6)
operation(1, 2, 3, 4, e=5, f=6)
operation(1, 2, 3, d=4, e=5, f=6)
operation(1, 2, c=3, d=4, e=5, f=6)
