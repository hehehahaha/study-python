#快排，递归
def quick_sort(arr, low, high):
     #temp = a[0]
     i = low
     j = high
     if i >= j:
          return arr
     temp = arr[i]
     while i < j:
          while i < j and arr[j] >= temp:
               j = j-1
          arr[i] = arr[j]
          while i < j and arr[i] <= temp:
               i = i + 1
          arr[j] = arr[i]
     arr[i] = temp
     quick_sort(arr, low, i-1)
     quick_sort(arr, j+1, high)
     return arr

#非递归
def quick_sort(arr, low, high):
   i = low 
   j = high
   if i >= j:
      return arr
   indexlist = []
   indexlist.append(i)
   indexlist.append(j)
   while len(indexlist) > 0:
      i = indexlist[0]
      j = indexlist[1]
      temp = arr[i]
      while i < j:
         while i < j and arr[j] >= temp:
            j -= 1
         arr[i] = arr[j]
         while i < j and arr[i] <= temp:
            i += 1
         arr[j] = arr[i]
      arr[i] = temp
      #quick_sort(arr, low, i-1)
      #quick_sort(arr, j+1, high)
      if i < indexlist[1]:
         indexlist.append(indexlist[0])
         indexlist.append(i-1)
      if i > indexlist[0]:
         indexlist.append(i+1)  
         indexlist.append(indexlist[1])         
      indexlist.pop(0)
      indexlist.pop(0)
   return arr


if __name__ == "__main__":
     a = [10, 3, -3, 6, 0, 1, 4, 5, 11, 8]
     quick_sort(a, 0, len(a)-1)
     print(a)
