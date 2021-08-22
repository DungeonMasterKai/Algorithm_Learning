# Based on several implementations viewed online.
def MergeSort(arr):
    mid = len(arr)//2
    if len(arr)>1:
        left = arr[:mid]
        MergeSort(left)
        right = arr[mid:]
        MergeSort(right)

        i=j=k= 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1

            k+=1


        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr

print(MergeSort([1,3,7,2,40]))

