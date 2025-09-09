# from MyMath.Algebra.Basic import add, mul
from _021_Packages.MyMath import add, mul

print(add(1, 2))
print(mul(1, 2))
# print(div(1, 2))

# from _020_Modules.greetings import greet, greetName
import _020_Modules.greetings as gr
gr.greet()
gr.greetName("Vivek")

# from 015_Closure import Exp_Factory  # <-- Fails to import modules starting with a digit
from _015_Closure import Exp_Factory
res = Exp_Factory(3)(2)
print(res)
