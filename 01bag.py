#01
N = 6
W = 21
def knapsack(N, W):
   B = [[0 for i in range(W)] for j in range(N)]
   w = [0, 2, 5, 4, 3, 9]
   v = [0, 3, 8, 5, 4, 10]
   for i in range(1,N):
      for j in range(1,W):
         if w[i] > j:
            B[i][j] = B[i-1][j]
         else:
            B[i][j] = max(B[i-1][j-w[i]] + v[i], B[i-1][j])
   return B[5][20]
a = knapsack(N, W)
print(a)
