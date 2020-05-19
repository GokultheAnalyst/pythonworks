'''
This Scrips Search a element in an unsorted array using recursive method. if elements exists then return -1 
This algorithm is relplica of merge sort algoirthm but instead of swapping a element. its just a return -1 if search elements found.
'''

def search_array(sublist,sval):
    if len(sublist) > 1:
        t=int(len(sublist)/2)
        print("Next function call sublistlength",t)
        lsublist_new=(sublist[:t])
        rsublist_new=(sublist[t:])
        print("left new sublist",lsublist_new)
        print("right new sublist",rsublist_new)
        if sublist==[]:
            return 0
        elif sublist:
            if sval==sublist[0] or sval==sublist[1]:
                print (sval,'search element found in a list')
                return -1
        search_array(lsublist_new,sval)
        search_array(rsublist_new,sval)


lis=[3,5,2,6,7,4,21,9]
print(search_array(lis,12))
