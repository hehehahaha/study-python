def heapsort(arr):
  n = len(arr)
  for i in range(n, -1, -1):
    max_heap(arr, n, i)
  for i in range(n-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    max_heap(arr, n, i)  
  return arr
  
def max_heap(arr, n, i):
  largest = i
  l = 2*i+1
  r = 2*i+2
  if l<n and arr[i]<arr[l]:
    largest = l
  if r<n and arr[largest]<arr[r]:
    largest = r
  if largest != i:
    arr[largest], arr[i] = arr[i], arr[largest]
    max_heap(arr, n, largest)
arr = [1,2,3,3,65]
print(heapsort(arr))
