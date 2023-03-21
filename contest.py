string = list(map(int, input().split()))
cond1 = all(string[i] <= string[i+1] for i, _ in enumerate(string[:-1]))
cond2 = all(string[i] >= string[i+1] for i, _ in enumerate(string[:-1]))
if cond1 or cond2:
    print('YES')
else:
    print('NO')