n = int(input())
nums = list(map(int, input().split()))
q = int(input())
s = []
count = 0
for j in range(q):
    t = list(map(int, input().split()))
    if len(t) == 3:
        nums.pop(t[1]-1)
        nums.insert(t[1]-1, t[2])
        for w in nums:
            count += w
        s.append(count)
        count = 0
        print(nums)
    if len(t) == 2:
        for y in range(t[1]):
            g = nums[n-1]
            nums.pop(n-1)
            nums.insert(0,g)
        for w in nums:
            count += w
        s.append(count)
        count = 0
        print(nums)
print(s)