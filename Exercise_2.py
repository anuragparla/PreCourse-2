'''
1) partition()
Time complexity: O(N)
Space complexity: O(1)

2) quickSort()
Time complexity: Best case O(NlogN) and worst case O(N^2)
Space complexity: Best case O(logN) and worst case O(N)
'''


# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1 

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivot_index = partition(arr, low, high)

        quickSort(arr, low,  pivot_index - 1)
        quickSort(arr,  pivot_index + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
