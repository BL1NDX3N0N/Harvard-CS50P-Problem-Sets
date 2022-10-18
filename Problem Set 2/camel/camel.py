# Instead of printing to the console and having to deal
# with line-endings it will be easier to implement via
# string manipulation.
buffer = ''

for c in input('camelCase: '):
    if c.islower():
        buffer += c
    else:
        buffer += '_' + c.lower()

print(buffer)