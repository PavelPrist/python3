#Program calculate seconds to numbers of days,hours,minutes,seconds. Ask input seconds.

sec = int(input('Input time in seconds='))

minutes = sec//60
add_seconds = sec%60
print('-- Minutes=',minutes,'; Seconds=',add_seconds,'.',sep='')

hours = minutes//60
add_minutes = minutes%60
print('-- Hours=',hours,'; Minutes=',add_minutes,'; Seconds=',add_seconds,'.',sep='')

days = hours//24
add_hours = hours%24
print('-- Days=',days,'; Hours=',add_hours,'; Minutes=',add_minutes,'; Seconds=',add_seconds,'.',sep='')

#86400 секунд в дне.
#3600  секунд в часе.

print(f'-- Days={days}; Hours={add_hours}; Minutes={add_minutes}; Seconds={add_seconds}.')

