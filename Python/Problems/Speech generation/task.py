x = input()
digits = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

for n in str(x):
    print(digits[int(n)])
