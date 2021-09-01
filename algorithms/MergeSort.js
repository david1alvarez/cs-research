function mergeSort(arr) {
  if (arr.length > 1) {
    let mid = Math.floor(arr.length)
    let l = arr.slice(0, mid)
    let r = arr.slice(mid, arr.length - 1)

    mergeSort(l)
    mergeSort(r)

    let i,j,k
    i = j = k = 0

    while (i < l.length && j < r.length) {
      if (l[i] < r[j]) {
        arr[k] = l[i]
        i++
        k++
      } else {
        arr[k] = r[j]
        j++
        k++
      }
    }

    while (i < l.length) {
      arr[k] = l[i]
      i++
      k++
    }

    while (j < r.length) {
      arr[k] = r[j]
      j++
      k++
    }
  }
}


/*
(0)             [20,5,1,3,5,2,15,20,900,13]
(1)    l[20,5,1,3,5]                 l[2,15,20,900,13]
(2)  l[20,5]     r[1,3,5]        l[2,15]       r[20,900,13]
(3)l[20]  r[5]  l[1]  r[3,5]   r[2]   l[5]   r[20]    l[900,30]  
(4)                  l[3] r[5]                       l[900] r[30]


In this algorithm, we follow the left side of the tree first.
Dividing the array into the smallest pieces, we arrive at (3)l of [20]
Since the array doesn't have a lenght > 1, we stop dividing and operate on it
from (2)l: [20,5], we have arrays of: l = [20], r = [5]

performing the merge sort on this yields:
  l[0] is not less than r[0], so we enter the `else` clause
  arr[0] = r[0], so now `(2)l: [20,5]` is [5,5]
  
  now i = 0, j = 1, k = 1, and since j == arr.length, we exit the first loop
  since i < arr.length, we enter the second loop:
    arr[k] = l[i], so now the original parent array is [5,20]

  We don't have any more accessible clauses in the function, so we exit this recursion step
*/
