


#unique paths using Recursions Version Source to target
i,j=0,0
counter=0
def movenext(i,j):
    global coutner
    print("Current value of i and j",i,j)
    if (i==3 and j==3):
        counter=1
        print(counter)
        return 1
    if (i>3 or j>3):
        print("loop execeed")
        return 0
    return movenext(i+1,j) + movenext(i,j+1)

#print(movenext(0,0))


#unique paths using Recursions Version target to source
i,j=0,0
def uniquePaths( m, n):
    #print("Current value of m and n",m,n)
    if (m==1 and n==1):
        #print("target reached")
        return 1
    if (m<=0 or n<=0):
        #print("loop execeed")
        return 0
    return uniquePaths(m-1,n) + uniquePaths(m,n-1)

#print(uniquePaths(23,12))


#unique paths using Recursions Version target to source
dict1={}
def uniquePaths3( m, n):
    print("Current value of m and n",m,n)
    print(dict.items())
    if (m,n) in dict1:
        return dict1[(m,n)]
    else:
        if (m==1 and n==1):
            return 1
        if (m<=0 or n<=0):
            return 0
        f1=uniquePaths3(m-1,n)
        dict1[(m-1,n)]=f1
        f2=uniquePaths3(m,n-1)
        dict1[(m,n-1)]=f2
        return f1+f2

print(uniquePaths3(3,2))

