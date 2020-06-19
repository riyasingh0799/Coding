"""
Max_Heapify(A, i)
It is assumed that subtrees rooted at i->left and i->right are max heaps but A[i] might be smaller than its children.
The value A[i] floats down the heap till heap rooted at i becomes a max heap.
"""


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
        print(arr[i])
        maxheapify(arr, largest, size)

A = [2, 17, 14, 6, 13, 10, 1]
maxheapify(A, 0, 7)
print(A)