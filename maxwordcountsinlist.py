# create a workd ferequency Dictory

list1 =["hello world is getting warmer unless govt is willing to do something or else world will be devasated will the govt will help to fix the issue or it going to me just a just a talk show in th world forum to try to say some thing to world to give somme temp happens"]

for i in list1:
    newli=list(i.split(' '))
print(list1)


dit1={}
gblmax=0
gblmaxkey=''
for key in newli:
    if key in dit1:
        dit1[key]= dit1[key]+1
        gblmax=max(gblmax,dit1[key])
        if (gblmax==dit1[key]):
            gblmaxkey=key
    else:
        dit1[key]=1 ## dit[key] assigns a counter value to the key
        if gblmax < 1:
            gblmax=1
            gblmaxkey=key

print(dit1.items())
print("gbl_max_key",gblmaxkey,gblmax)
