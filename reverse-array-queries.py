# Reverse Array Queries

# For a given array of integers, perform operations on the array. Return the resulting array after all operations have been applied in the order given.
# Each oepration contains two indices. Reverse the subarray between those zero-based indices, inclusive.

# Example
# arr = [9,8,7,6,5,4,3,2,1,0]
# operations = [[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]
# return: [9,1,7,3,5,4,6,2,8,0]
def performOperations(arr, operations):
    for operation in operations:
        start = operation[0]
        end = operation[1] + 1
        arr[start:end] = reversed(arr[start:end])

        return arr