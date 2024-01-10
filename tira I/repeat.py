def find(s: str):
    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            sub_s = s[0 : i]
            found = True
            for j in range(1, len(s) // i):
                asdf = s[j * i : j * i + i]
                if s[j * i : j * i + i] != sub_s: found = False
            if found: return len(sub_s)