def bubble_sort(arr):
     length = len(arr)
     while length > 0:   
          for i in range(length-1):
               if arr[i] > a[i+1]:
                    arr[i] = arr[i] + arr[i+1]
                    arr[i+1] = arr[i] - arr[i+1]
                    arr[i] = arr[i] - arr[i+1]
          length -= 1

if __name__ == "__main__":
     a = [10, 3, -3, 6, 0, 1, 4, 5, 11, 8]
     bubble_sort(a)
     print(a)
     
