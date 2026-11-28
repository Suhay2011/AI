def reversing(s):
    if len(s) == 1:
        return s[0]
    firstchar =s[0]
    return reversing(s[1:]) + firstchar
s ="Anna"
print(reversing(s))
