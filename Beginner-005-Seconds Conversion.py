s= int(input())
d= s // (24 * 60 * 60)
r= s % (24 * 60 * 60)
h= r // (60 * 60)
r= r % (60 * 60)
m= r // 60
s= r % 60
print(f'{d}D{h}H{m}M{s}S')
