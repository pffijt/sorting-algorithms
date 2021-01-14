'''
    Heap sort
    Created by: Pepijn Fijt
    Complexity: Θ(n log n)
'''

arr = [2,5,8,1,3,4,99,1099, 123]
heap_size = 0

def parent(i):
    return int(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def max_heapify(arr, i):
    global heap_size
    l = left(i)
    r = right(i)
    if(l < heap_size and arr[l] > arr[i]):
        largest = l
    else:
        largest = i
    if(r < heap_size and arr[r] > arr[largest]):
        largest = r
    if(largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest)

def build_max_heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(int((len(arr) - 1) / 2), -1, -1):
        max_heapify(arr, i)

def heap_sort(arr):
    global heap_size
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size = heap_size - 1
        max_heapify(arr, 0)
    return arr
