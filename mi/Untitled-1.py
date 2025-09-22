
ln = [0.7,0.2,0.01]
lc = [0.8,0.1,0.7]
A = [0.4,0.4,0.2]

result = [0,0,0]
denum = [0,0,0]
temp = 0
temp2 = 0

for a in range(len(A)):
    result[a] += A[a]
    result[a] *= 1-lc[a]
    result[a] *= ln[a]
    
    temp += result[a]

    print(result[a])
    print(1-result[a])
    print(" ")

    denum[a] = A[a]
    denum[a] *= 1-lc[a]
    temp2 += denum[a]
    print(result[a]/denum[a])
    print(" ")


print(temp/temp2)