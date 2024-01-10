def count(t,k):
    nums = {}
    result = []
    for i in t[0:k]:
        if i not in nums:
            nums[i] = 0
        nums[i] += 1
    result.append(len(nums))
    for i in range(len(t)-k):
        if t[i+k] not in nums:
            nums[t[i+k]] = 0
        nums[t[i+k]] += 1
        nums[t[i]] -= 1
        if nums[t[i]] == 0:
            nums.pop(t[i])
        result.append(len(nums))
    return result