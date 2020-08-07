year = int(input())

if year % 400 == 0:
    print("Leap")
elif year % 100 == 0:
    print("Ordinary")
elif year % 4 == 0:
    print("Leap")
else:
    print("Ordinary")
