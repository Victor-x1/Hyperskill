inp = int(input())

if inp > 1:
    for i in range(2, inp):
        if (inp % i) == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")

else:
    print("This number is not prime")
