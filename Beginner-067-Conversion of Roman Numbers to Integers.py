from sys import stdin

def roman_to_decimal(roman):
    values= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total= 0
    prev= 0
    
    for char in reversed(roman):
        value= values[char]
        if value<prev:
            total-= value
        else:
            total+= value
        prev= value
    
    return total

lines= stdin.read().strip().split('\n')
n= int(lines[0])
for i in range(1, n + 1):
    roman = lines[i].strip()
    print(roman_to_decimal(roman))
