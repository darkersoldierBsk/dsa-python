'''
How it works:

Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.
'''
#MAIN VERSION O(n^2) time consuming 

arr = [23, 45, 15, 2, 56 , 33, 20]

n = len(arr)

for i in range(n-1):
    min_index = i
    
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    min_value = arr.pop(min_index)
    
    arr.insert(i, min_value)


print("Sorted array:", arr)

#OPTIMISED VERSION O(n^2) less time consuming

arr = [23, 45, 15, 2, 56 , 33, 20]

n = len(arr)

for i in range(n):
    min_index = i
    
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j   
            
    arr[i], arr[min_index] = arr[min_index], arr[i]  #swapping values instead of pop()ping and insert()ing


print("Sorted array:", arr)
