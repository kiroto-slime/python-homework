A= {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
    'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
    'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
    'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
    'Z': 33
}
def id_number(id_str):
    if (len(id_str)!= 10 or id_str[0] not in A or 
        id_str[1] not in "12" or not id_str[2:].isdigit()):
        return "0"
    val= A[id_str[0]]
    n1, n2= val//10, val%10
    weights= [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total= n1*weights[0]+n2*weights[1]+sum(int(id_str[i])*weights[i+1] for i in range(1, 10))
    return "1" if total%10== 0 else "0"
n= int(input())
for e in range(n):
    print(id_number(input().strip()))
