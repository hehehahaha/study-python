#0往后排
l = [1, 2, 0, 0, 4, 0, 0, 1, 0]
noZeros=-1
for i in range(len(l)):
   if (l[i] != 0):
      noZeros += 1
      if (i != noZeros):
         l[i], l[noZeros] = l[noZeros], l[i]
print(l)
