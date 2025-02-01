import ast
def r(num):
    return [list(r) for r in zip(*num[::-1])]

x = input()
num = ast.literal_eval(x)
r = r(num)
print(str(r).replace(' ', ''))
