def arrayTotalSum(a):

    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arrayTotalSum(a[1:])

a = [1,5,7,9]
print("Array total sum:", arrayTotalSum(a))
