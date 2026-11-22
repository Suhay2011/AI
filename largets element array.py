def MAXElementArray(a):
    length = len(a)
    if length == 1:
        return a[0]

    return max(a[0],MAXElementArray(a[1:]))

a = [3,4,6,9,10,13,15,256,712]
print("Largest element of array: ", MAXElementArray(a))
