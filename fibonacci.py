
        
print('Lowest value: ', minVal) # Step 4 - Print the min. value
//First 20 Fibonacci numbers

//TIP 1 - LOOP SOLUTION
//Define two variables:
//First one is for the record of the previous Fibonacci number
//The second one is for the sum of the prev1 and prev2

prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

for i in range(18):            // 0 to 18
    newFibo = prev1 + prev2
    print(newFibo)
    prev1 = prev2
    prev2 = newFibo


//TIP2 - RECURSION SOLUTION
//
print(0)
print(1)
count = 2

def fibo(prev2, prev1):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev1 = prev2
        prev2 = newFibo
        count += 1
        fibonacci(prev2, prev1)
    else:
        return

fibo(1,0)


//TIP2.1 - RECURSION SOLUTION FOR THE Nth ELEMENT
//Now same problem with recursion
//The mathematic formula for this is : F(n) = F(n-1) + F(n-2)
//It means our last element is sum of 2 previous elements

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))
