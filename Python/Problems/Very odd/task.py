# put your python code here
A, B, = (int(input()) for i in range(2))
C = (int(A / B))

if C % 2 == 0:
    print("False")
else:
    print('True')
