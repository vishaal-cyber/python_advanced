#region Function Declaration #################

# def add(a: int, b: int) -> int:
#     sum = a + b
#     return sum

# print(add("Test", "String"))

#endregion

#region Define Earlier (not Higher) #####################

# def Foo():
#     print("Foo called")
#     Bar()

# def Main():
#     print("Main called")
#     Foo()

# def Bar():
#     print("Bar called")

# Main()


# #--C-Code---------------------------------

# # void Bar(int);

# # void Foo()
# # {
# #     printf("Foo called");
# #     Bar(x);
# # }

# # void Bar(int x)
# # {
# #     printf("Bar called");
# # }

# # void main()
# # {
# #     printf("main called");
# #     Bar();
# # }

#endregion ####################

#region DocStrings ######################################

#################################
# author: Ramakant
# purpose: add to values (numerical addition / string concatenations)
# IN: accepts two values
# RET: added/concatenated value
##################################

# def add(a, b):
#     """
#     author: Ramakant
#     purpose: add to values (numerical addition / string concatenations)
#     IN: accepts two values
#     RET: added/concatenated value
#     """
#     sum = a + b
#     return sum, a-b

# print(add(1, 2))
# print(add.__doc__)

#endregion  #############################


#region Arg Passing ################################

# def add(a, b):                       # Positional Args
#     print(f"{a = },  {b = }")
#     sum = a + b
#     return sum

# print(add(1, 2))



# # def add(a, b, c = 0):                       # Default Args; Non-default argument should NOT follow default argument
# def add(a, b=0, c=0):                       # Default Args
#     print(f"{a = },  {b = }, {c = }")
#     sum = a + b + c
#     return sum

# print(add(1, 2))
# print(add(1, 2, 3))



# def Sub(a, b):
#     return a - b

# print(Sub(7, 5))
# print(Sub(a = 7, b = 5))        # Named Arg; KeyWorded args
# print(Sub(b = 5, a = 7))        # Named Arg


#endregion #########################################


#region Arguments (Packing, Unpacking, Variable Args, KwVariable Args )###############################################################

# # lst = [1, 2]
# # lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# a = lst
# print(f"{type(a) = }")

# # p, q = lst  # Unpacking
# # p, q, r = lst  # Unpacking
# # p, _, r = lst  # Unpacking
# # p, q, r, s = lst  # Unpacking
# p, _, _, _, t = lst  # Unpacking

# # lst = [1, 2]
# p, *others, t = lst


# print(f"{type(p) = }, {p = }")
# print(f"{type(t) = }, {t = }")
# print(f"{type(others) = }, {others = }")


# a, b, c = 1, 2, 3


# def add(a, b):
#     return a + b


# # print(add(1, 2))


# x, y = 1, 2
# print(add(x, y))


# lst = [1, 2]
# print(add(lst[0], lst[1]))

# # print(add(lst))    # a, b = lst   <--- Not implied 
# print(add(*lst))    # <-- Unpacking the list to supply for the arguments



# *new_lst = 1, 2, 3



#----------------------------------------------


# # Variable Arguments
# def add (a, b, *c):     # <-- Package all values other than the first 2, into c (as a collection)
#     sum = a + b
#     print(f"{type(c) = }, {c = }")

#     for val in c:
#         sum += val

#     return sum

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))

# lst2 = [1, 2, 3, 4, 5, 6, 7]
# print(add(*lst2))



# # Keyworded Variable Args
# def PrintEmp(ceo, cfo, **others):
#     print(f"[{ceo = }, {cfo = }]")
#     for pos, emp in others.items():
#         print(f"{pos} = {emp}")


# PrintEmp("Manish", "Abhijeet")
# PrintEmp("Manish", cfo="Abhijeet")
# # PrintEmp(ceo="Manish", "Abhijeet")      # <-- Wn't work; Named arg can NOT be before Positional arg
# PrintEmp(ceo="Manish", cfo="Abhijeet")
# PrintEmp(ceo="Manish", cfo="Abhijeet", cto="Pravin")
# PrintEmp("Manish", "Abhijeet", cto="Pravin")


#endregion ###########################################################


#region Scope ########################################
## LEGB --> Local, External, Global, Builtins

# def Foo():
#     global s
#     s = "Modified String"
#     print(f"Foo --> {s}")

# s = "Global String"

# Foo()
# print(f"Global --> {s}")


#-----------------------------------

# def Outer():
#     # global s
#     print(f"{locals() = }")
#     s = "Outer String"

#     def Inner():
#         # global s
#         # nonlocal s
#         s = "Inner String"
#         print(f"Inner --> {s}")

#     Inner()
#     print(f"Outer --> {s}")

#     print(f"{globals() = }")
#     # print(f"Testing --> {globals()['s']}")
#     globals()['s'] = "Modified Global"

# s = "Global String"

# Outer()
# print(f"Global --> {s}")

#----------------------------------------------------


def Outer():
    s = "Outer String"

    def Inner():
        s = "Inner String"
        print(f"Inner --> {s}")

    print(f"Outer --> {s}")
    return Inner


s = "Global String"

fn = Outer()
print(f"Global --> {s}")

fn()

print("-"*25)
Outer()()

#endregion ######################################

# Need to discuss 'Closure' at some point

