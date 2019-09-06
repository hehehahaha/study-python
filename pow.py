#暴力
class Solution:
    def myPow(self, x: float, n: int) -> float:
        judge = True
        if n<0:
            n = -n
            judge = False
        if n==0:
            return 1
        final = 1     # 记录当前的乘积值
        tmp = x       # 记录当前的因子
        count = 1     # 记录当前的因子是底数的多少倍
        while n>0:
            if n>=count:
                final *= tmp  
                tmp = tmp*x
                n -= count
                count +=1  
            else:
                tmp /= x
                count -= 1
        return final if judge else 1/final

#根据奇偶幂分类
#递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            return 1/self.help_(x,n)
        return self.help_(x,n)

    def help_(self,x,n):
        if n==0:
            return 1
        if n%2 == 0:  #如果是偶数
            return self.help_(x*x, n//2)
        # 如果是奇数
        return self.help_(x*x,(n-1)//2)*x


#迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:      
        judge = True
        if n < 0:
            n = -n
            judge = False     
        final = 1
        while n>0:
            if n%2 == 0:
                x *=x
                n //= 2
            final *= x
            n -= 1
        return final if judge else 1/final
