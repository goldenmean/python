'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45
'''


def timeConversion(s):
    # Write your code here
    if s.endswith("PM"):
        a = s.split(":")
        hr=int(a[0])
        mn=int(a[1])
        sc=a[2]
        se=int(sc[0:2])
        if hr!= 12:
            reshr=hr+12
        else:
            reshr=hr
        resmin=mn
        ressec=se
        
        strhr=str(reshr).zfill(2)
        strmn=str(resmin).zfill(2)
        strse=str(ressec).zfill(2)
        
        return strhr+":"+strmn+":"+strse
    else:
        a = s.split(":")
        hr=int(a[0])
        mn=int(a[1])
        sc=a[2]
        se=int(sc[0:2])
        if hr == 12:
            reshr=0
        else:
            reshr=hr
        resmin=mn
        ressec=se
        
        strhr=str(reshr).zfill(2)
        strmn=str(resmin).zfill(2)
        strse=str(ressec).zfill(2)
        
        return strhr+":"+strmn+":"+strse
        

#s="07:05:45PM"
#s="8:03:00AM"
s="12:00:00PM"
#s='07:34:12PM'

print(s)
print(timeConversion(s))

		