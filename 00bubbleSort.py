'''
Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.
'''

arr = [1,9,3,37,23]           #create an array

size = len(arr)               #get the length of the array

for i in range(size-1):       #in our example it's 0 to 4

    swapped = False           #for optimization 1

    for j in range(size -i -1):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j] #swapping the values of our value and the next smaller value
            swapped = True   #for optimization 2

    if not swapped:           #for optimization 3
        break                 #for optimization 4


print("Sorted array : ", arr)     


'''
Bubble Sort Algorithm Step by Step Changes

Step 0 - [1,9,3] -> our array , 

Step 1 - [1,9,3]   (i = 0), 1 and 9 checked nothing changed , swapped = False

Step 2 - [1,3,9]   (i = 0), 9 and 3 checked and they swapped the values, swapped = True

Step 3 - [1,3,9]   (i = 1), 1 and 3 checked nothing changed, swapped = False

Step 4 - break -   (since no swaps in Step 3)

Step 5 - print the array
'''
