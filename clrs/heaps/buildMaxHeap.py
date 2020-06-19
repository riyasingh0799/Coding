def maxheapify(arr, i, size) :
    if i>size:
        return
    largest = i
    if 2*i+1 < size and arr[2*i+1] > arr[i]:
        largest = 2*i+1
    if 2*i+2 < size and arr[2*i+2] > arr[largest]:
        largest = 2*i+2
    if largest!=i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxheapify(arr, largest, size)

def buildMaxHeap(A, size):
    for i in range(int(size/2)-1, -1, -1):
        maxheapify(A, i, size)

A = [2, 14, 1, 66, 13, 11, 10]
buildMaxHeap(A, 7)
print(A)