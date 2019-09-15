def Fibonacci(n):
  s = [] * n
  s.append(1)
  s.append(1)
  for i in range(2, n):
    s.append(s[i-1]+s[i-2])
  return s[n-1]
print(Fibonacci(10))
        
        
#递归        
let num = 0;    // 用来记录fib函数执行次数，执行一次加一
function fib(n) {
  num ++;
  if(n === 0) {
    return 0;
  }
  if(n === 1) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
}
