'''
S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8]
Explanation:
There are five guests attending the party.
The 1st guest will arrive at time 1. We need one chair at time 1.
The 2nd guest will arrive at time 2. There are now two guests at the party, so we need two chairs at time 2.
The 5th guest will arrive at time 3. There are now three guests at the party, so we need three chairs at time 3.
The 4th guest will arrive at time 5 and, at the same moment, the 1st and 2nd guests will leave the party.
There are now two (the 4th and 5th) guests at the party, so we need two chairs at time 5.
The 3rd guest will arrive at time 6, and the 4th guest will leave the party at the same time.
There are now two (the 3rd and 5th) guests at the party, so we need two chairs at time 6.
So we need at least 3 chairs.
'''
#S = [1, 2,4, 6, 5, 3,6,5,1]
#E = [5, 5,5,7, 6, 6,7,9,9]
S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
##S.sort()
##E.sort()
mins=0
print(S)
for i in S:
    if i not in E:
        mins +=1
    else: E.remove(i)

    print("value of i",i,"value of min",mins)


print(mins)
## Algorithm
##parsing each start time and Add chair
##check for any one leaving at same start time remove a chair
