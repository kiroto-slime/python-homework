A= {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
    'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
    'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
    'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
    'Z': 33
}
def id_letters(num_str):
    letters= []
    for letter in sorted(A.keys()):
        val= A[letter]
        n1, n2= val//10, val%10
        weights= [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        total= n1*weights[0] + n2*weights[1]
        
        for index, digit in enumerate(num_str):
            total+= int(digit) * weights[index+2]
        if total%10== 0:
            letters.append(letter)
    
    return "".join(letters)
n = int(input())
for i in range(n):
    digits= input().strip()
    print(id_letters(digits))
