#找零钱
def num(arr, val):
   out = [0] * (val+1)
   for i in range(1, 1+val):
      temp = val
      for j in arr:
         if i-j >= 0:
            temp = min(temp, out[i-j] + 1)
      out[i] = temp 

   return out[-1]

a = num([186,419,83,408],6249)
print(a)
