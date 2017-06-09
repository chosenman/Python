def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in range(len(arr)):
        print x
        arr[x] *= num
        print arr
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b