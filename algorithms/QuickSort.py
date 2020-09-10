def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    print(f'new partition, pivot is {pivot}')

    # iterate through the list once, moving two pointers: i points to the first element of the list that is smaller than
    # the pivot, while j points to the element of the list that is being assessed. When an instance is found such that arr[i]
    # is less than or equal to the pivot, swap it for the arr[i+1] value, and move i up to point to that new value. Effectively 
    # iterating through the list with an upper and lower index bounds, and whenever the upper index bound finds a value less 
    # than or equal to the pivot, place it where the lower bound is, and move the lower bound up. This process ensures that at
    # the end of the list, all elements that are equal to or lower than the pivot will be safely at or behind the lower index bound.
    # Once that is the case, swap the pivot with the element that is one above i, ensuring that all elements equal to or lower than
    # the pivot will be to the left of it, and all elements greater than it will be to the right of it. The order of those domains
    # doesnt matter, as the point of the partitioning is to find the sorted index of the pivot.
    # Partitioning in this way also mutates the array, so we can use the new somewhat-sorted array in our next iterations.
    for j in range(low, high):
        print(f'i={i}, j={j}, arr={arr}')
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap elements

    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(f'the final partition array is {arr}, with the pivot at index {i+1}')
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) <= 1:
        return arr
    
    if low < high:
        partitionIndex = partition(arr, low, high)

        quickSort(arr, low, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)