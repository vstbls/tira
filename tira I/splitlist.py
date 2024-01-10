def count(t: list):
    smallest = t[-1]
    mins = [smallest]
    for i in range(len(t)-2, -1, -1):
        if t[i] < smallest:
            smallest = t[i]
        mins.append(smallest)
    mins.reverse()
    print(mins)

    largest = t[0]
    result = 0
    for i in range(len(t)-1):
        if t[i] > largest:
            largest = t[i]
        if mins[i+1] > largest:
            result += 1
    return result

print(count([1,2,3,1,2,2,3,1,4,2,3,5]))