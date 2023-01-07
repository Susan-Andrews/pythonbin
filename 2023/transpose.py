a=[[4,8] , [3,19] , [15,6]]
trans=[[0,0,0] , [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        trans[j][i]=a[i][j]
for k in trans:
    print(k)        
