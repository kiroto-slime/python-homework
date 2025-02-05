while True:
    try:
        a = input().strip()
        b = input().strip()
        if not a or not b:
            print()
            continue
        result = []
        for i in sorted(set(a) & set(b)):
            result.extend([i] * min(a.count(i), b.count(i)))
        print("".join(result))
    except EOFError:
        break
