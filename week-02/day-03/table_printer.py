# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def table_printer(dict_in_list):

	ingreds = list()
	cool = list()
	stock = list()

	ingredsline = 0
	coolingline = len(' Needs Cooling ')
	instockline = len(' In Stock ')

	for lst in ingredients:
		ingrname = lst.get('name')
		ingreds.append(ingrname)
		if len(ingrname) > len('Ingredients'):
			ingredsline = len(ingrname) + 2
		else:
			continue

	for c in ingredients:
		coolset = c.get('needs_cooling')
		if coolset == True:
			coolset = 'yes'
		else:
			coolset = 'no'
		cool.append(coolset)
	for inst in ingredients:
		stocking = inst.get('in_stock')
		if stocking ==0:
			stocking = '-'
		else: 
			stocking = str(stocking)
		stock.append(stocking)
		
	print('+' + '-' * ingredsline + '+' + '-' * coolingline + '+' + '-' * instockline + '+')
	print('|' + ' ' + 'Ingredients' + ' ' * (ingredsline - len('ingredients') - 1) + '|' + ' ' + 'Needs Cooling' + ' ' + '|' + ' ' + 'In stock' + ' ' + '|')
	print('+' + '-' * ingredsline + '+' + '-' * coolingline + '+' + '-' * instockline + '+')

	for z in range(len(ingredients)):
		print('|' + ' ' + ingreds[z] + ' ' * (ingredsline - len(ingreds[z])-1) + '|' + ' ' + cool[z] + ' ' * (coolingline - len(cool[z])-1) + '|' + ' ' + stock[z] + ' ' * (instockline - len(stock[z])-1) + '|')
	print('+' + '-' * ingredsline + '+' + '-' * coolingline + '+' + '-' * instockline + '+')



table_printer(ingredients)
    