vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

# Once again easier to implement via string manipulation
# in lieu of dealing with line-endings.
buffer = ''

for c in input('Input: '):
    if c not in vowels:
        buffer += c

print(buffer)