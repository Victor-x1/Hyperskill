# Converted to String List
pasta = ["tomato", "basil", "garlic", "salt", "pasta", "olive oil"]
apple_pie = ["apple", "sugar", "salt", "cinnamon", "flour", "egg", "butter"]
chocolate_cake = ["chocolate", "sugar", "salt", "flour", "coffee", "butter"]
omelette = ["egg", "milk", "bacon", "tomato", "salt", "pepper"]

ratatouille = ["aubergine", "carrot", "onion", "tomato", "garlic",
               "olive oil", "pepper", "salt"]
# Input
ingredient = input()

# Pasta
count = pasta.count(ingredient)
if count > 0:
    print('pasta time!')
# Apple Pie
count = apple_pie.count(ingredient)
if count > 0:
    print('apple pie time!')
# Ratatouille
count = ratatouille.count(ingredient)
if count > 0:
    print('ratatouille time!')
# Chocolate Cake
count = chocolate_cake.count(ingredient)
if count > 0:
    print('chocolate cake time!')
# Omelette
count = omelette.count(ingredient)
if count > 0:
    print('omelette time!')
