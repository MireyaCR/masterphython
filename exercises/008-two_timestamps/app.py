#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    hour = hr1 * 3600
    min = min1 * 60
    total_first = hour + min + sec1
    hour = hr2 * 3600
    min = min2 * 60
    total_second = hour + min + sec2
    
    return total_second - total_first
    return None


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))