// can we get the first number by adding numbers from the other array?
// think through it by seeing if recursively subtracting elements of the arr
// from the input number to see if you can reach 0
const canSumRecursive = (targetSum, numbers) => {
  if (targetSum === 0) return true;
  if (targetSum < 0) return false;

  for (let num of numbers) {
    const remainder = targetSum - num;
    if (canSumRecursive(remainder, numbers) === true) {
      return true;
    }
  }

  return false
}

const canSumMemoized = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return true;
  if (targetSum < 0) return false;

  for (let num of numbers) {
    const remainder = targetSum - num;
    if (canSumMemoized(remainder, numbers) === true) {
      memo[targetSum] = true
      return true;
    }
  }

  memo[targetSum] = false
  return false
}

console.log(canSumMemoized(300, [7,5]))
