
def QuickSort(arr):
    def partition(arr):
        pivot = arr[-1]
        left = []
        right = []
        match = False
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            elif i == pivot and match == False:
                match = True
            elif i == pivot and match:
                left.append(i)
        return left, right
    if len(arr) >= 1:
        left, right = partition(arr)
        left = QuickSort(left)
        right = QuickSort(right)
        return left + [arr[-1]] + right
    else:
        return arr

print(QuickSort([1,3,8,10,2,4,90, 4]))

