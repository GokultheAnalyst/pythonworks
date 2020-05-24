'''
Fibonannci Series using Dyanamic programing
Steps:
1. find the sub problemns and count the of sub problems
2.Guess
3. recuurences
4.recursive/memoize - bottom up
   Acylic - Top order
5. algorithm to  solve original problems

fibonacci 0,1,1,2,3,5,8,13,21,34
index     0,1,2,3,4,5,6, 7, 8, 9
n =0 then 0
n =1 then 1 
'''

## Recursive Approch of Fibnonaci ()
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if n > 1:
        n1=fib(n-1)
        n2=fib(n-2)
        return n1+n2

print(fib(5)) # return 8
# Fibonnaci Version 1
memo_dit={} # define a dictionary in outside of function
def memo_fib(n):
    #memo_dit={} #Stores the previous computed value
    if n in memo_dit:
        return memo_dit[n]
    if n == 0:
        memo_dit[n]=0
        return memo_dit[n]
    if n == 1:
        memo_dit[n]=1
        return memo_dit[n]
    if n > 1:
        return memo_fib(n-1) + memo_fib(n-2)


print(memo_fib(5)) # return 8

# Fibonnaci Version 2

memo_dit=[0]*10 # define a dictionary in outside of function
def memo_fib2(n):
    print("loppin on n value{} , and list",n,memo_dit)
    if n == memo_dit[n]:
        print("ins ret n loppin on n value{} , and list",n,memo_dit)
        return memo_dit[n]
    if n == 0:
        memo_dit[n]=0
        print("ins ret 0 loppin on n value{} , and list",n,memo_dit)
        return memo_dit[n]
    if n == 1:
        memo_dit[n]=1
        print("ins ret 1 loppin on n value{} , and list",n,memo_dit)
        return memo_dit[n]
    if n > 1:
        return memo_fib2(n-1) + memo_fib2(n-2)

print(memo_fib2(8)) # return 8

