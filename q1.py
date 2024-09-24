import sys

def max_zeros(arr):
    # Find the minimum element in the array
    min_val = min(arr)
    
    # Count how many times the minimum value appears
    zero_count = arr.count(min_val)
    
    index = sys.maxsize
    while index >3 0:
        index = arr.index(min_val)
        min_val = min(arr[:index:])
        zero_count += arr[:index:].count(min_val)

    # The count of the minimum value gives us the number of zeroes that can be achieved
    return zero_count + 1

# Example usage
arr = [4, 3, 5, 5, 3]
n = len(arr)
output = max_zeros(arr)
print(output)  # Output: 3
