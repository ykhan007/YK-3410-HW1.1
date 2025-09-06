import random
import timeit

# Linear Search with operation counter
def linear_search(arr, target):
    ops = 0
    for i, val in enumerate(arr):
        ops += 1  # counting comparison
        if val == target:
            return i, ops
    return None, ops

# Binary Search with operation counter
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    ops = 0
    while left <= right:
        ops += 1  # comparison count
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, ops
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None, ops

# Make array of 200 random numbers
arr = random.sample(range(1, 1000), 200)
arr_sorted = sorted(arr)

# Pick a number that is in the array and one that is not
present = random.choice(arr)
absent = -1

# Timing function
def time_search(func, arr, target, trials=1000):
    t = timeit.timeit(lambda: func(arr, target), number=trials)
    return (t / trials) * 1_000_000  # microseconds

# Run timing tests
print("=== Search Timing (μs per call) ===")
print(f"Linear (present): {time_search(linear_search, arr, present):.3f}")
print(f"Binary (present): {time_search(binary_search, arr_sorted, present):.3f}")
print(f"Linear (absent): {time_search(linear_search, arr, absent):.3f}")
print(f"Binary (absent): {time_search(binary_search, arr_sorted, absent):.3f}")
