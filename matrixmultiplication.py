m=[[5, 7],
    [8, 6]]    
n=[[5, 7],
  [8, 6,]]
result=[[0, 0],
        [0, 0]]
for i in range(len(m)):

    for j in range(len(n[0])):

        for k in range(len(n)):
            result[i][j] += m[i][k]*n[k][j]
 
for r in result:
    print(r)
