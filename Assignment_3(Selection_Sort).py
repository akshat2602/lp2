# Implement Greedy Search Algorithm for: Selection Sort

def sort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if(arr[minIndex] > arr[j]):
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(arr)


arr = [5, 2, 1, 3, 4, 1, 1, 1]
sort(arr)
