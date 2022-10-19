a = [1,2,6,9,0,19]

def recSum(arr, index):
    if index >= len(arr):
        return 0
    return recSum(arr,index+1) + arr[index]

print(recSum(a,0))