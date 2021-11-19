print("*************heapsort**************")

def heapify (arr,n,i):
    root = i
    l = i*2+1 
    r = i*2+2
    if l<n and arr[root]<arr[l]:
        root = l
    if r<n and arr[root]<arr[r]:
        root = r
    if root!=i:
        arr[root],arr[i] = arr[i],arr[root]
        heapify(arr,n,root)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 -1 ,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    
def display(arr):
    for i in range(len(arr)):
        print(arr[i],end=",")
    print()

     

arr = [44, 3, 6, 4, 7, 1, 9, 3, 2, 51, 2]
heapsort(arr)
display(arr)
