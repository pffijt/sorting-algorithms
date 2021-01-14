import datetime
from random import sample
from ctypes import CDLL, c_int
from heap_sort import heap_sort

so_file = './sort/heap_sort.so'
heap_sort_c = CDLL(so_file)
arr = sample(range(20_000_000), k=10_000)
arrc = arr[:]
arrt = arr[:]

print('heap sort')
first_time = datetime.datetime.now()
heap_sort(arr)
later_time = datetime.datetime.now()
duration = later_time - first_time
print(duration.total_seconds())

print('Heap sort in c')
first_time = datetime.datetime.now()
c_arr = (c_int * len(arrc))(*arrc)
heap_sort_c.heapSort(c_arr, 4)
later_time = datetime.datetime.now()
duration = later_time - first_time
print(duration.total_seconds())

print('default Timsort')
first_time = datetime.datetime.now()
arrt.sort()
later_time = datetime.datetime.now()
duration = later_time - first_time
print(duration.total_seconds())
