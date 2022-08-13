"""
Great for solving a problem by breaking it down into much smaller problems. Like math problems. 
1.Take a large problem
2. Break into subproblem
3. use the sub problem to find a solution then apply to the larger problem




Tabulation: Solve the bigger problem by working from the bottom up. work from BOTTOM UP

Memoization: Solve the bigger problem by recursively finding the solution of the sub problems. Work from TOP DOWN. 





Tabulation              Memoization
Easier                     Harder
Runtime slower           Faster run time
Uses stack space       Stack is not used a lot
Quick solution         Efficent solution

"""

def fibonnaciTab(n):
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])   #working from bottom up 
    return tb[n-1]

print("Fibonnaci squence for 6 with tabulation: " , fibonnaciTab(6))


#Fib with memoization
#Time complexity O(n), Space complexity O(n)

# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will, edge cases
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0, edge case
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)    #recursive call fib(n-1) + (n-2)


print("Fibonnaci squence for 6 with memoization: " , Fibonacci(6))




