hour1, min1, sec1, hour2, min2, sec2 = (int(input()) for i in range(6))  
print((hour2 - hour1) * 3600 + (min2 - min1) * 60 + (sec2 - sec1))
