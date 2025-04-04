N = input()
placeholding = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in placeholding:
    N = N.replace(i, '*')
print(len(N))