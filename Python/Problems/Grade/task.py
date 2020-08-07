grade, top = (float(input()) for i in range(2))

score = grade / top

if score >= 0.90:
    print("A")
elif 0.80 <= score < 0.90:
    print("B")
elif 0.70 <= score < 0.80:
    print("C")
elif 0.60 <= score < 0.70:
    print("D")
elif score < 0.59:
    print("F")
