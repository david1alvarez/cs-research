// super slow, O(2^(n+m))
const gridTravelerRecursive = (m, n) => {
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;

  return gridTravelerRecursive(m - 1, n) + gridTravelerRecursive(m, n - 1);
}

// O(n*m)
// this could be improved by memoizing based on the fact that 
// traversal through a x,y sized grid is the same
// as traversing through a y,x sized grid (1,2 == 2,1)
const gridTravelerMemoized = (m, n, memo = {}) => {
  const key = m + "," + n
  if (key in memo) return memo[key]
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;

  memo[key] = gridTravelerMemoized(m - 1, n, memo) + gridTravelerMemoized(m, n - 1, memo);
  return memo[key]
}

console.log(gridTravelerMemoized(1, 1))
console.log(gridTravelerMemoized(2, 3))
console.log(gridTravelerMemoized(3, 2))
console.log(gridTravelerMemoized(3, 3))
console.log(gridTravelerMemoized(18, 18))
