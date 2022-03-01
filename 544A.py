start = list(map(int, input().split(":")))
stop = list(map(int, input().split(":")))

if stop[0] > start[0]:
    min_diff = stop[1] - start[1] + 60* (stop[0] - start[0])
    mid_diff = int(min_diff / 2)
    mid_min = start[1] + mid_diff
    mid_hour = start[0]
    if mid_min >= 60:
        mid_hour = start[0] + mid_min // 60
        mid_min = mid_min % 60

else:
    min_diff = stop[1] - start[1]
    mid_diff = int(min_diff / 2)
    mid_min = start[1] + mid_diff
    mid_hour = start[0]

if mid_min //10 == 0:
    mid_min = '0'+str(mid_min)
if mid_hour // 10 == 0:
    mid_hour = '0'+str(mid_hour)
    
print(f"{mid_hour}:{mid_min}")