def Bar():
    print("Bar")
    n = 7
    d = 0
    if d == 0:
        # raise ValueError("A value of '0' is unacceptabe for a denominator.")
        raise TypeError("A value of '0' is unacceptabe for a denominator.")
    q = n/d
    print(q)

    print("Returning from Bar")

def Foo():
    print("Foo")
    try:
        Bar()
    # except OverflowError as ex:
    #     print(f"Logging the exception of type {type(ex)}, and notifying the user on UI")
    except (TypeError, OverflowError) as ex:
        print(f"Logging the exception of type {type(ex)}, and notifying the user on UI")
    except ValueError as ex:
        # print(ex) --> print(str(ex))  --> print(ex.__str__())
        print(f"There was an exception --> {ex!r}.") # print(repr(ex)) # --> print(ex.__repr__())
    except Exception as ex:
        print("Generic Exception in Bar", f" - [{type(ex)}] - {ex}")
        # raise Exception("Fresh Data")
        # raise
    finally:
        print("The 'Finally' block to follow 'Bar'")
    print("Returning from Foo")

def Main():
    print("Main")
    Foo()
    print("Returning from Main")

if __name__ == "__main__":
    Main()

print("Back in the Global Scope")