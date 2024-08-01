




from itertools import permutations

n = 4513

# convert the number to string
num = str(n)

# generate all permutations of digits
perms = permutations(num)

res = []
# print the permutations
for perm in perms:
    res.append(int(''.join(perm)))

print(res)
