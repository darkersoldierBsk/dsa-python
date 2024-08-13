#Lowest in an Array

#TIP1 - INDEXING
arr = [2, 8, 12, 100]
minVal = arr[0]      # Step 1 - Create a min.value var and set it to the first element of the array

for i in arr:        # Step 2 - Go through every element of the array
    if i < minVal:   # Step 3 - If the current element is lower than the min. value, set current as the minVal
        minVal = i
        
print('Lowest value: ', minVal) # Step 4 - Print the min. value