def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

def eval(s: str):
    l = s.split(" ")
    ops = []
    for i in l:
        if i[0] == "(":
            ops.append((i[1], []))
        elif i[-1] == ")":
            ops[-1][1].append(int(i.replace(")", "")))
            for _ in range(i.count(")")):
                o = ops.pop()
                if o[0] == "+":
                    calc = sum(o[1])
                else:
                    calc = prod(o[1])
                if len(ops) > 0:
                    ops[-1][1].append(calc)
                else:
                    return calc
        else:
            ops[-1][1].append(int(i))

if __name__ == "__main__":
    print(eval("(+ 7 4 (* 5 8 0 (* 6 1)) (+ 1 9 (* 6 7)))")) # 63
    print(eval("(+ 1 2 3 4 5)")) # 15
    print(eval("(+ 5 (* 3 2) 7)")) # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168
    print(eval("(+ 123 456)")) # 579