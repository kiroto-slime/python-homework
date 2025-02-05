a = {
    'A': (1, 0), 'B': (1, 1), 'C': (1, 2), 'D': (1, 3), 'E': (1, 4),
    'F': (1, 5), 'G': (1, 6), 'H': (1, 7), 'I': (3, 4), 'J': (1, 8),
    'K': (1, 9), 'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (3, 5),
    'P': (2, 3), 'Q': (2, 4), 'R': (2, 5), 'S': (2, 6), 'T': (2, 7),
    'U': (2, 8), 'V': (2, 9), 'W': (3, 2), 'X': (3, 0), 'Y': (3, 1),
    'Z': (3, 3)
}
n = int(input())
test = [input().strip() for i in range(n)]

def validate(id_num):
    if len(id_num) != 10:
        return "0"
    if id_num[0] not in a:
        return "0"
    if id_num[1] not in '12':
        return "0"
    if not id_num[2:].isdigit():
        return "0"
    region_digits = a[id_num[0]]
    n1, n2 = region_digits
    digits = [n1, n2] + [int(c) for c in id_num[1:]]
    
    w = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total = sum(d * w for d, w in zip(digits, w))
    return "1" if total % 10 == 0 else "0"
results = [validate(tc) for tc in test]
print("\n".join(results))
