# Not related to loops and would have been an excellent example
# problem for working with available APIs to pull said dataset.
fruits = {
    'apple' : '130',
    'avocado' : '50',
    'banana' : '110',
    'cantaloupe' : '50',
    'grapefruit' : '60',
    'grapes' : '90',
    'honeydew melon' : '50',
    'kiwifruit' : '90',
    'lemon' : '15',
    'lime' : '20',
    'nectarine' : '60',
    'orange' : '80',
    'peach' : '60',
    'pear' : '100',
    'pineapple' : '50',
    'plums' : '70',
    'strawbaerries' : '50',
    'sweet cherries' : '100',
    'tangerine' : '50',
    'watermelon' : '80'
}

item = input('Item: ').strip().lower()

if item in fruits:
    print('Calories: ' + fruits[item])