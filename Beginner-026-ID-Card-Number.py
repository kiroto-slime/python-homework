a = {
    'A': (1, 0), 'B': (1, 1), 'C': (1, 2), 'D': (1, 3), 'E': (1, 4),
    'F': (1, 5), 'G': (1, 6), 'H': (1, 7), 'I': (3, 4), 'J': (1, 8),
    'K': (1, 9), 'L': (2, 0), 'M': (2, 1), 'N': (2, 2), 'O': (3, 5),
    'P': (2, 3), 'Q': (2, 4), 'R': (2, 5), 'S': (2, 6), 'T': (2, 7),
    'U': (2, 8), 'V': (2, 9), 'W': (3, 2), 'X': (3, 0), 'Y': (3, 1),
    'Z': (3, 3)
}

n = int(input())
test_cases = [input().strip() for _ in range(n)]

def validate_id_number(id_number):
    if len(id_number) != 10:
        return "F"
    if id_number[0] not in a:
        return "F"
    if id_number[1] not in '12':
        return "F"
    if not id_number[2:].isdigit():
        return "F"
    # 轉換英文字母為對應的數字
    region_digits = a[id_number[0]]
    n1, n2 = region_digits
    # 將身份證號碼轉換成數字陣列
    digits = [n1, n2] + [int(c) for c in id_number[1:]]
    # 加權公式
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total = sum(d * w for d, w in zip(digits, weights))
    # 驗證結果
    return "T" if total % 10 == 0 else "F"
# 處理每筆測試資料
results = [validate_id_number(tc) for tc in test_cases]
# 輸出結果
print("\n".join(results))
