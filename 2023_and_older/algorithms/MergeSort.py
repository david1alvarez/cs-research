def mergeSort(arr): # sort by in-place mutation of array
    if len(arr) > 1: # only operate a sort on arrays where length > 1
        mid = len(arr) // 2 # find the midpoint of the array (rounded down)
        L = arr[:mid] # take the leftmost elements of the array
        R = arr[mid:] # take the rightmost elements of the array

        mergeSort(L) # sort the leftmost elements of the array
        mergeSort(R) # sort the rightmost elements of the array

        i = j = k = 0 # set place counters to 0
        while i < len(L) and j < len(R): # run through the two arrays until reaching the end of one of them
            if L[i] < R[j]: # if the ith element of the left list is less than the jth element of the right list:
                arr[k] = L[i] # set the kth element of the array being sorted to the ith element of the left array
                i += 1 # increment the element in the left array
                k += 1 # increment the element of the array being sorted
            else: # if the ith element of the left list is not smaller than the jth element of the right list:
                arr[k] = R[j] # set the kth element of the array being sorted to the jth element of the right array
                j += 1 # increment the element of the right array
                k += 1 # increment the element of the array being sorted
        
        # add the remaining elements the left or right arrays to the end of the array being sorted
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [20,5,1,3,5,2,15,20,900,13]
mergeSort(arr) # modify arr
print(arr)