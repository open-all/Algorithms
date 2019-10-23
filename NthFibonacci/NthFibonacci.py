import time
# O(2^n) time | O(n) space
def fibRecursiveNaive(n):
    """naive recurive implementation of fibonacci"""
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibRecursiveNaive(n - 1) + fibRecursiveNaive(n - 2)

# O(n) time | O(n) space
def fibRecursiveMemoized(n , memoize = {1: 0, 2: 1}):
    "efficient interative approach to finding fibonacci numbers"
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fibRecursiveMemoized(n - 1, memoize) + fibRecursiveMemoized\
        (n - 2, memoize)
        return memoize[n]

# O(n) time | O(1) space
def fibIter(n):
    "efficient interative approach to finding fibonacci numbers"
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

def main():
    #simple tests to compare the speed of each implementation
    start = time.clock()
    print(fibRecursiveNaive(35))
    print("process executed in ", time.clock() - start, "seconds")

    start = time.clock()
    print(fibRecursiveMemoized(35))
    print("process executed in ", time.clock() - start, "seconds")

    start = time.clock()
    print(fibIter(35))
    print("process executed in ", time.clock() - start, "seconds")

if __name__ == "__main__":
    main()
