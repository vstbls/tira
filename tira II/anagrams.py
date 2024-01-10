def create(s):
    s = sorted(s)
    result = set()
    used = [False for i in s]
    def r(str):
        if len(str) == len(s):
            result.add(str)
        for i in range(len(s)):
            if not used[i]:
                used[i] = True
                r(str+s[i])
                used[i] = False
    r('')
    return sorted(list(result))

import string

def add(anagram, original, result):
    if len(anagram) == len(original):
        result.append(anagram)
    for letter in string.ascii_lowercase:
        if anagram.count(letter) < original.count(letter):
            add(anagram+letter, original, result)
 
def create2(s):
    result = []
    add("", s, result)
    return result

from time import time

t1 = time()
print(len(create("lakdjfoief")))
t2 = time()
print(len(create2("lakdjfoief")))
t3 = time()
print(t2-t1, t3-t2)