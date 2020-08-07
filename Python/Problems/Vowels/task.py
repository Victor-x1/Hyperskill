word = input()
vowels = 'aeiou'

# create your list here
output = ''.join([x for x in word if x in vowels])

# Converts string to list
print(f'{list(output)}')
