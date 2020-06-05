problemset : https://leetcode.com/problems/two-city-scheduling/

lis=[[10,20],[30,200],[400,50],[30,20],[130,90],[290,130],[890,420],[450,900],[1000,10],[10,60]]
#lis=[[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
sublis=[]
for j in lis:
    print([j[0],j[1],min(j),abs(j[0]-j[1])])
    sublis.append([j[0],j[1],min(j),abs(j[0]-j[1])])

sublis.sort(key = lambda x: x[3] ,reverse=1) ## used to the sort a array based on Key
print(sublis)
counterA=0
fsum=0
counterB=0
max_lim1=int(len(lis)/2)
print(max_lim1)
for i in sublis:
    if (i[0]==i[2] and counterA < max_lim1) or (i[1]==i[2] and counterB >= max_lim1):
        counterA +=1
        fsum +=i[0]
        print("cityA",counterA,"value",i[0])
    else:
        counterB +=1
        fsum +=i[1]
        print("cityB",counterB,"value",i[1])




print(counterA,counterB,fsum)
