
#数组重复
def nonrepeat(list0):
   list1= []       #创建一个新的数组
   for element in list0 :
       if(element not in list1):
           list1.append(element)
   print (list1)

list0 = [1,2,13,1,31,21,13,1,3,13,1,31,211,1]
nonrepeat(list0)
