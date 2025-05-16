import ast
def r(num):
    return [list(r) for r in zip(*reversed(num))]

x= input()
num= ast.literal_eval(x)
print(str(r(num)).replace(' ', ''))
