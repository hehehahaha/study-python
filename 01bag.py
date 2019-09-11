#01
import numpy as np
N = 6
W = 21
def knapsack(N, W):
   B = np.ones((N,W))*0
   w = [0, 2, 5, 4, 3, 9]
   v = [0, 3, 8, 5, 4, 10]
   for i in range(1,N):
      for j in range(1,W):
         if w[i] > j:
            B[i][j] = B[i-1][j]
         else:
            value1 = B[i-1][j-w[i]] + v[i]
            value2 = B[i-1][j]
            if value1 > value2:
               B[i][j] = value1
            else:
               B[i][j] = value2
   return B[5][20]
a = knapsack(N, W)
print(a)
