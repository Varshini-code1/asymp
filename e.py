def aMean(arr, s):
    sum = 0
    for i in range(0, s):
        sum += arr[i]
    return float(sum/s)

def aMed(arr, s):
    sorted(arr)
    if s % 2 != 0:
        return float(arr[int(s/2)])
    return float((arr[int((s-1)/2)] + arr[int(s/2)])/2.0)

arr = [1,4,5,2,5,8,5,2,6,8]
s = len(arr)