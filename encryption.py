def compute():
    d = {}
    for c in (65, 97): # 'A' and 'a'
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    return d

d = compute()

s = "Hello Encryption"
print("Encrypted:", "".join([d.get(c, c) for c in s]))
print(d)