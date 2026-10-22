arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def max_sum(arr, k):
    curr_sum = 0
    maxi = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]  # Add the current element
        
        # Once we hit the window size k
        if i >= k - 1:
            maxi = max(maxi, curr_sum)
            outgoing_element = arr[i - k + 1]
            curr_sum -= outgoing_element  # Remove the element sliding out
            
    return maxi

print(max_sum(arr, 2))  # Output: 17 (8 + 9)