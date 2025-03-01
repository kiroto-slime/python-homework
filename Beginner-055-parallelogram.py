import sys
from collections import Counter
for line in sys.stdin:
    try:
        nums=list(map(float, line.split()))
        if len(nums) != 8:
            continue
    except:
        continue
    c=Counter((nums[i], nums[i+1]) for i in range(0, 8, 2))
    rep=[p for p in c if c[p]== 2]#重複的
    if len(rep) != 1:
        continue
    unq=[p for p in c if c[p]==1]#沒重複的
    if len(unq) != 2:
        continue
    r=rep[0]
    A, B=unq
    D=(A[0]+B[0]-r[0], A[1]+B[1]-r[1])
    print(f"{D[0]:.3f} {D[1]:.3f}")
