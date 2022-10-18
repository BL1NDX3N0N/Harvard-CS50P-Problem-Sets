items = {}

def PrintSortedItems():
    for item, amount in sorted(items.items()):
        print(f'{amount} {item}')

while True:
    try:
        item = input().strip().upper()

        if item not in items:
            items[item] = 1
        else:
            items[item] += 1

    except EOFError:
        print()
        PrintSortedItems()
        break