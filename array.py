arr=[1,2,3,2,1]
n=len(arr)
def array1(arr,n):
    for i in range(len(arr)):
        if arr.count(i) > 1:
            return arr[i]
print(array1(arr, n))
