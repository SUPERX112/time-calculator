def add_time(start, duration, day=''):
    PM=False
    if 'PM' in start or 'pm' in start:
        PM=True

    new_time=''
    z=0
    period=''
    
    new1=dividi_AMPM(start)
    new1[0]=dividi_d(new1[0])
    
    new2=dividi_d(duration)
    
    if int(new2[0])+ int(new2[1]) == 0:
        return start

    if int(new2[0])>=24:
        z=int(new2[0])%24
    else:
        z=int(new2[0])
        
    new_h=int(new1[0][0])+int(z)
    sum_h1_h2=float(new1[0][0])+float(new2[0])
    
    new_m=int(new1[0][1])+int(new2[1])
    while int(new_m)>=60:
        new_h+=1
        new_m-=60
        sum_h1_h2=float(new_h)+float(new2[0])
        
    if int(new_m)<10:
        new_m='0'+str(new_m)
        
    if PM:
        period=' PM'
        new_time=create_time(new_h,new_m, sum_h1_h2, period, day)
        return new_time

    if not PM:
        period=' AM'
        new_time=create_time(new_h,new_m, sum_h1_h2, period, day)
        return new_time
     

def dividi_AMPM(time):
    new=''
    if 'PM' in time:
        new=time.split('PM')
    elif 'pm' in time:
        new=time.split('pm')
    if 'AM' in time:
        new=time.split('AM')
    elif 'am' in time:
        new=time.split('am')
    return new

def dividi_d(duration):
    new=duration.split(':')
    return new

def create_time(h,m,sum_h,t,d):
    new_time=''
    day_p=''
    day_p=how_many_days(sum_h,t)
    day_d=which_day(d,sum_h)
    if int(h)<12:
        if int(h)<10:
            new_time=str(h)+':'+str(m)+t+day_d+day_p
            return new_time
        else:
            new_time=str(h)+':'+str(m)+t+day_d+day_p
            return new_line
    while int(h)>12:
        h-=12
    if t==' PM' or t=='pm':
        t=' AM'
    else:
        t=' PM'
    if int(h)<10:
        new_time=str(h)+':'+str(m)+t+day_d+day_p
        return new_time
    else:
        new_time=str(h)+':'+str(m)+t+day_d+day_p
    return new_time

def day_count(h,t):
    b=int(h)
    if h<24 and t==' AM':
        return 0
    else:
        day=round(b/24)
        return day


def day_count2(h):
    b=int(h)
    day=round(b/24)
    return day


def how_many_days(h2,t):
    n=int(day_count(h2,t))
    if n!= 0 and n!= 1:
        day_p=f' ({n} days later)'
        return day_p
    elif n == 1:
        day_p=' (next day)'
        return day_p
    else:
        day_p=''
        return day_p

def which_day(day,h): 
    days=[', Monday',', Tuesday',', Wednesday',', Thursday',', Friday',', Saturday',', Sunday']
    days_2=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    day=day.upper()
    count=0
    count2=0
    h=day_count2(h)
    if day != '':
        for d in days_2:
            if day in d:
                break
            else:
                count+=1
    else:
        return day
    count2=h+count
    while count2>=7:
        count2-=7

    return days[count2]            
    
    
