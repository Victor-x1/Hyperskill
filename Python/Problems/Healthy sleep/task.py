A, B, H = (int(input()) for i in range(3))

# A - Recommended Hours
# B - Should not sleep more than A
# H = hours a day
# A = less than A = Deficiency, more than B = Excess

if H <= A:
    print("Deficiency")

if H >= B:
    print("Excess")

if A <= H <= B:
    print("Normal")
