import math

input = [[1,5],[0,14]]
weight_1 = [[1.3,-0.3],[1.7,1]]
weight_2 = [0.6,-1.4]
input_iteration = 0
hidden = [0,0]

def sig(x):
    return 1/(1+math.exp(-x))

result = 0
for i in range(2):
    for j in range(2):
        hidden[i] += input[input_iteration][j]*weight_1[i][j]
    
    hidden[i] = sig(hidden[i])

for i in range(2):
    result += hidden[i]*weight_2[i]
result = sig(result)


print(result)


