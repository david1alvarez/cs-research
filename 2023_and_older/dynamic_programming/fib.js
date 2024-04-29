// fairly straighforward, but takes a long time as n->inf
// O(2^n) time complexity
const fibRecursive = (n) => {
  if (n <= 2) {
    return 1;
  }
  return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// memoization: storing previously-computed values
// create a quickly-accessible data structure to store a key:value pair
const fibMemoized = (n, memo = {}) => {
  if (n in memo) return memo[n]
  if (n <= 2) {
    return 1;
  }
  memo[n] = fibMemoized(n - 1, memo) + fibMemoized(n - 2, memo);
  return memo[n]
}

// solve iteratively by building a table (an array)
// in the fibonacci sequence, you can construct an array of values
// by iterating throug the array and adding the values to the next two indices
// [0,1,1,2,3,5,8]
// gives us a time and space complexity of O(n)
const fibTabulated = (n) => {
  const table = Array(n+1).fill(0);
  table[1] = 1;

  for (let i = 0; i <= n; i++) {
    
  }
}


console.log(fibMemoized(50))
