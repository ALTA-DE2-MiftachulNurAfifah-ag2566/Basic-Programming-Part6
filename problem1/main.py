def compare(a, b):
    pattern = ""
    a = list(a)
    b = list(b)
    # print(a, b)
    if len(a) < len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                continue
            else:
                pattern += a[i]
    else:
        for i in range(len(b)):
            if a[i] != b[i]:
                continue
            else:
                pattern += a[i]
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA