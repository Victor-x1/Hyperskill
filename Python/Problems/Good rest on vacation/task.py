# put your python code here
duration, food, flight, hotel = (int(input()) for i in range(4))
print(int(duration * food) + (flight * 2) + (hotel * (duration - 1)))
