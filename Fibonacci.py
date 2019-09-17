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
 
def Fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  f0, f1 = 0, 1
  f = 0
  for i in range(2, n+1):
    f = f0 + f1
    f0 = f1
    f1 = f
  return f

print(Fibonacci(10))
