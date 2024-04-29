import time
# Recurision is a technique where a function calls itself to solve a problem.
# It is most useful for divide-and-conquer problems, where a problem can best 
# be solved from the top down by breaking it into smaller problems.

# The base case is the condition that stops the recursion. Without a base case,
# the function will continue to call itself indefinitely.

# The recursive case is the condition that calls the function itself. This is
# where the problem is broken down into smaller problems.

# The classic example of recursion is calcilating the value of a fibonacci function output for large numbers.
# This is due to the fact that the fibonacci function is defined as the sum of the two previous numbers in the sequence,
# which is a recursive definition. A purely recursive implementation of the fibonacci function is very slow, as it recalculates
# the same values many times. A more efficient implementation uses memoization, which stores the results of previous calculations.
# We will use this in the subsequent example.

# The following is a recursive implementation of the fibonacci function without memoization.
def recursive_fibonacci(n: int) -> int:
    # base case:
    if n <= 1:
        return 1
    # recursive case:
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# time complexity calculation: there is a constant time evaluation at each node of the created recursive call tree
# the tree is "complete", which is to say that each path proceeds all the way down to the same terminal root value
# each level of the tree has two times as many nodes as the previous level. The change factor here is the number of
# recursive calls that the method makes (2). The series 1 + 2 + 4 + ... + 2^(n-2) + 2^(n-1) + 2^n simplifies in big-O
# notation to O(2^n). This is firmly in the "bad" category for large-value performance.

print("the 5th fibonacci sequence value is:", recursive_fibonacci(5))
print("un-memoized performance at high values is quite slow however.")
print("calculating the 40th place value...")
start: float = time.time()
large_fibonacci: int = recursive_fibonacci(40)
end: float = time.time()
print("it took", (end - start), "seconds to calculate the value of", large_fibonacci)
print("Larger numbers take much longer because the time complexity of this is 2^n. To get around issues like fibonacci(100) taking 2^60 times longer than fibonacci(40), we'll use memoization")

memo: dict = {}
def memoized_recursive_fibonacci(n: int) -> int:
    # base case:
    if n <= 1:
        return 1
    # memo case:
    if n in memo:
        return memo[n]
    # recursive case:
    result = memoized_recursive_fibonacci(n - 1) + memoized_recursive_fibonacci(n - 2)
    memo[n] = result
    return result

# When we memoize the equation, we prevent the vast majority of recursive nodes from being needed. The depth stays the same,
# as each value in the tree will still need to be calculated, but because the time complexity of the non-memoized method 
# comes from the presence of many repeated nodes, removing repeat calculations helps a lot. We wind up needing to calculate
# each value O(n) times. The "left"-most branch is complete, but as we move up the tree and calculate each node's "right" 
# operation, we can see that the node's second/"right" operation has already been calculated, and can be acccessed with O(c)
# time complexity. For each value, we need to perform 2 constant-time calculations, so we have O(2n) which is just O(n). The
# recursive depth remains the same however, which requires a relatively large allocation space.

print("calculating the 999th fibonacci value using memoization...")
start = time.time()
large_fibonacci = memoized_recursive_fibonacci(999)
end = time.time()
print("our memoized method only took", (end - start), "seconds to calculate the value of", large_fibonacci)
print("However, this generates a recursive call stack that has a space complexity of O(n). Python's default maximum is 1000. From a top-down approach, there is no direct way around this as we need to \"descend\" through the number of the position argument one by one. If space complexity is your primary concern, then recursion might not be the best way to handle this challenge.")
print("we can use a bottom-up iterative method to work around this limit however, using constant space.")

def iterative_fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    x_2_prior: int = 0
    x_1_prior: int = 1
    x: int = 0
    for _ in range(2, n):
        x = x_2_prior + x_1_prior
        x_2_prior = x_1_prior
        x_1_prior = x
    return x

# Here however, we have function whose time and space complexity has been sufficiently reduced. We do not need to
# store unnecessary values in a memo, because we do not need to revisit previous calculations in the algorithm.
# The calculation processes through each integer value leading up to the desired position once, using a constant-time
# calculation at each step. The space complexity is a constant O(c), and the time complexity is O(n).

print("Calculating the 10,000th position of the fibonacci sequence...")

start = time.time()
large_fibonacci = iterative_fibonacci(10000)
end = time.time()

print("it took", (end - start), "seconds to calculate value of", large_fibonacci)

print("\nHere we can see how a bottom-up approach is much more performant than a top-down approach. The fibonacci sequence serves not only as a great teaching example for recursive programming and memoization, but also as a reminder that sometimes simpler methods are better.")