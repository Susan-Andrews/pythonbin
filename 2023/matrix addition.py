a=[[4,8,18],[3,19,12] ,[15,6,9]]
b=[[8,32,23] , [12,1,15] ,[5,12,3]]

sum_of_mat=[[0,0,0] ,[0,0,0] , [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        sum_of_mat[i][j]=a[i][j]+b[i][j]
for k in sum_of_mat:
    print(k)
