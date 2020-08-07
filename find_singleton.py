def singleNumber(nums):
    seen = set()

    for elm in nums:  # O(n)
        if elm not in seen:  # O(1) bec set()
            seen.add(elm)  # O(1)
        else:
            seen.remove(elm)  # O(1)

    return seen.pop()  # O(1)


print(singleNumber([2, 2, 1]))

# seen = {}

# for i in range(len(nums)):   #O(n)
#     if nums[i] not in seen:
#         seen[nums[i]] = 1
#     else:
#         seen[nums[i]] += 1

# for val in seen:            #O(n)
#     if seen[val] == 1:
#         return val

# total O(2n) -> O(n)