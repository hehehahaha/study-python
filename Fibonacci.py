def Fibonacci(n):
  s = [] * n
  s.append(1)
  s.append(1)
  for i in range(2, n+1):
    s.append(s[i-1]+s[i-2])
  return s[n]

#递归
def Fibonacci(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return Fibonacci(n-1) + Fibonacci(n-2)
  
print(Fibonacci(10))
