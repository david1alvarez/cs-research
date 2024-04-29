/* Question: How does Quick Sort work?
Answer: Select a pivot. The pivot should be the number closest to the halfway point ideally,
to minimize time, but since we don't have information on the ordering of the list lets just take 
the last item. Each iteration, we work through the list and identify the number of items in the list that 
are smaller than the selected pivot, recording this here as i. The way this works out in the code is that
arr[i] is always left pointing to the highest number that is smaller than the pivot, and that any time arr[j]
comes across a new number smaller than the pivot, we bump i up and swap arr[i] with arr[j]. This ensures that 
as we move through the list we keep the "safe" numbers in the indexes equal to or below i, and only increment i 
when we have a new number to be added to that collection. When we reach the end of the list, we have the pivot
correctly placed, with all numbers lower than it to it's left, and all numbers higher than it to its right. 

We then pass the pivot's location (i) to two more calls of the function, and run through everything again!

Question: Why does it make things faster to pick a number that that is in the middle?
Answer: The fewer times we need to iterate through the array the better. The best case number of 
iterations through the array is log(n), and if each time we divide the array perfectly in half then it 
becomes a balanced tree, with each level containing n elements. Iterating through every element in this tree
results in passing through n*log(n) elements

Question: Why are the best and average case scenarios the same time complexity?
Answer: I don't recall the exact proof, but I remember it had to do with the fact that big O
notation is a simplified representation of the actual time complexity, and represents the time
complexity as n approaches an arbitrarily large number. It was something like 2n*log(n) for the average
case, which becomes O(n*log(n))
*/


function partition(arr, low, high) {
  // i indicates the index of an element smaller than the pivot,
  // and the winds up being the correct location of the pivot found so far
  let i = low - 1;
  let pivot = arr[high];

  for(let j = low; j < high; j++) {
    // if the current element is smaller than the pivot
    if (arr[j] <= pivot) { // the <= is important, < would never sort the pivot into place
      i++; // increment the index of Smaller Element
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i+1], arr[high]] = [arr[high], arr[i+1]];

  return i+1
}

function quickSort(arr, low, high) {
  if (arr.length <= 1) {
    return arr
  }

  if (low < high) {
    const partitionIndex = partition(arr, low, high) 

    quickSort(arr, low, partitionIndex - 1)
    quickSort(arr, partitionIndex + 1, high)
  }
}

/*
let arr = [10, 7, 8, 9, 1, 5]
let n = arr.length
quickSort(arr, 0, n-1)
print(arr)
*/
