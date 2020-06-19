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

def heapsort(A, size):
    for i in range(size-1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        size-=1
        maxheapify(A, 0, size)

A = [5,13,2,25,7,17,20,8,4]
buildMaxHeap(A, 9)
heapsort(A, 9)
print(A)