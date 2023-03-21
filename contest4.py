n = int(input())
a = list(map(int, input().split()))
nums = {}
seq = n
for l in range(n):
    el = a[l]
    if el not in nums:
        nums[el] = 0
    nums[el]+= 1
    vals = nums.values()
    mini = min(vals)
    if len(set(vals))==2:
        if mini == 1 and list(vals).count(1)==1:
            seq = l+1
        elif max(vals) - mini == 1 and list(vals).count(max(vals))==1:
            seq = l+1
print(seq)