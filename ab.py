#A个a，B个b
A = 3
B = 8
flaga = 0
flagb = 0
while A>0 and B>0:
   if (A>=B or flagb == 2) and flaga !=2:  # A>B或者B已经写2次了 且 A不能写超过2次
      print('a')
      A -= 1
      flaga += 1
      flagb = 0
   else:
      print('b')
      B -= 1
      flagb += 1
      flaga = 0
#有剩的
if (A != 0):
   for i in range(A):
      print('a')
if (B != 0):
   for i in range(B):
      print('b')
