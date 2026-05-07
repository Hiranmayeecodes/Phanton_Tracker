'''
Cyber Crime Investigation using
Searching and Sorting Algorithms
'''

'''
Transaction Data
'''
transactions = [120, 45, 300, 220, 90, 600,
                130, 75, 800, 500, 350, 40]

threshold = 250


'''
Objective 1
Linear Search for Suspicious Transactions
'''
def linear_search_suspicious(transactions, threshold):

    suspicious = []

    for amount in transactions:

        if amount > threshold:
            suspicious.append(amount)

    return suspicious


'''
Objective 2
Selection Sort
'''
def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        '''
        Swap elements
        '''
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


'''
Objective 3
Binary Search
'''
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return False


'''
Objective 4
Merge Sort
'''
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


'''
Merge Function
'''
def merge(left, right):

    sorted_list = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1

        else:
            sorted_list.append(right[j])
            j += 1

    '''
    Add remaining elements
    '''
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


'''
Driver Code
'''

'''
Objective 1
Find suspicious transactions
'''
suspicious_transactions = linear_search_suspicious(
    transactions,
    threshold
)

print("Suspicious Transactions:")
print(suspicious_transactions)


'''
Objective 2
Sort suspicious transactions
'''
sorted_suspicious = selection_sort(
    suspicious_transactions.copy()
)

print("\nSorted Suspicious Transactions:")
print(sorted_suspicious)


'''
Objective 3
Search for transaction amount 500
'''
search_amount = 500

found = binary_search(
    sorted_suspicious,
    search_amount
)

print("\nTransaction 500 Found:")
print(found)


'''
Objective 4
Merge Sort all transactions
'''
sorted_transactions = merge_sort(transactions)

print("\nFully Sorted Transactions:")
print(sorted_transactions)


'''
Time Complexity Analysis

1. Linear Search
Time Complexity = O(n)

2. Selection Sort
Time Complexity = O(n^2)

3. Binary Search
Time Complexity = O(log n)

4. Merge Sort
Time Complexity = O(n log n)
'''