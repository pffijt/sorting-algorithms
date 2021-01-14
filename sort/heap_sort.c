/*
    Heap sort
    Created by: Pepijn Fijt
    Complexity: Θ(n log n)
*/

#include <stdio.h>

int heapSize;

int parent(int i) {
    return i / 2;
}

int left(int i) {
    return 2 * i;
}

int right(int i) {
    return (2 * i) + 1;
}

void maxHeapify(int arr[], int i) {
    int l = left(i);
    int r = right(i);
    int largest;

    if (l < heapSize && arr[l] > arr[i]) {
        largest = l;
    } else {
        largest = i;
    }

    if (r < heapSize && arr[r] > arr[largest]){
        largest = r;
    }

    if (largest != i) {
        int temp = arr[largest];
        arr[largest] = arr[i];
        arr[i] = temp;
        maxHeapify(arr, largest);
    }
}

void buildMaxHeap(int arr[], int arrSize) {
    heapSize = arrSize;
    int halfArrSize = (arrSize - 1) / 2;
    for (int i = halfArrSize; i >= 0; --i) {
        maxHeapify(arr, i);
    }
}

void heapSort(int arr[], int arrSize) {
    buildMaxHeap(arr, arrSize);
    for (int i = arrSize - 1; i >= 0; --i) {
        int temp = arr[i];
        arr[i] = arr[0];
        arr[0] = temp;
        heapSize = heapSize - 1;
        maxHeapify(arr, 0);
    }
}
