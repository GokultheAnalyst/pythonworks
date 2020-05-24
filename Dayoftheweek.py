##This uses Standard metrics based on the Total Days from start date with module 7 
## Get the day of the week for the start year. 

def wk(day: int, month: int, year: int):
    int_year=1969
    leapyear=0
    if year%4==0: leapyear=1
    yr_cnt=year-int_year
    print ('year_cnt',yr_cnt)
        Tdays=(yr_cnt*365)+(yr_cnt//4)
    print ('total days',Tdays,"leap year cnt",(yr_cnt//4))
    mdayd=0
    for i in range(1,month):
        if i in (1,3,5,7,8,10,12):
            mdayd=mdayd+31
        elif i==2:
            mdayd=mdayd+28+leapyear
        else:
            mdayd=mdayd+30

    Final_days=Tdays+mdayd+(day-1)
    dayofweek = { 2:'friday', 3: 'saturday',4: 'sunday',5: 'monday', 6: 'tuesday',0: 'wednesday',1: 'thrusday' }
    f = dayofweek.get(Final_days%7)
    return f


print(wk(20,5,2020))


