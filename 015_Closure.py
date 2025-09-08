def Exp_Factory(power):
    def Inner(num):
        return num ** power
    return Inner


fn1 = Exp_Factory(2)
fn2 = Exp_Factory(3)
fn3 = Exp_Factory(4)



print(f"{fn1(10) = }")
print(f"{fn2(10) = }")
print(f"{fn3(10) = }")

# print("-"*25)
# Exp_Factory()()