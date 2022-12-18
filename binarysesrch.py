def binary_search(arr, target):
    # Let us set the lower and upper bounds 
    lower = 0
    high = len(arr) - 1

    # using Loop until the bounds converge
    while lower <= high:
        # Find the midpoint of the current search bounds
        mid = (lower + high) // 2
        
        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid
        
        # If the target value is less than the value at the midpoint then search the left half
        elif arr[mid] > target:
            high = mid - 1
        
        # If the target value is greater than the value at the midpoint then search the right half
        else:
            lower = mid + 1
    
    # If the target value is not found, return 0
    return 0

# To test the given function 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)
