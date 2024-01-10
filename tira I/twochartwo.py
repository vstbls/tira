def count(s: str):
    cur = s[-1]
    prev_i = len(s) # Maybe change this back to -1 depending on how you implement the rest
    char_indices = [prev_i]
    for i in range(len(s)-1, 0, -1):
        if s[i-1] != cur:
            cur = s[i-1]
            prev_i = i
        char_indices.append(prev_i)
    char_indices.reverse()
    print(char_indices)
    
    result = 0
    for i in range(len(s)):
        c = s[i]
        c_i = char_indices[i]
        if c_i < len(s):
            c2 = s[c_i]
            result += 1
            while s[char_indices[c_i]] in [c, c2]:
                c_i2 = char_indices[c_i]
                c_i = char_indices[c_i2]
                result += c_i - c_i2


    for i in range(len(s)):
        c = s[i]
        c_i = char_indices[i]
        if c_i < len(s):
            c2 = s[c_i]
            result += 1
            if char_indices[c_i] < len(s):
                while s[char_indices[c_i]] in [c, c2]:
                    c_i2 = c_i
                    c_i = char_indices[c_i]
                    result += c_i - c_i2
                    if char_indices[c_i] >= len(s):
                        break
                    if s[char_indices[c_i]] not in [c, c2]:
                        result += char_indices[c_i] - c_i - 1
    return result

if __name__ == "__main__":
    print(count("aaaa")) # 0
    print(count("caadaadaa"))
    print(count("abab")) # 6 [1,2,3,-1]
    print(count("aabacba")) # 8 [2,2,3,4,5,6,-1]
    print(count("abacaadbaacaa")) # 21 [1,2,3,4,5,5,6,7,8,8,9,-1,-1]