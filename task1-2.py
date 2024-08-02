def read_cook_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            num_ingredients = int(file.readline().strip())
            ingredients = []
            for i in range(num_ingredients):
                ingredient = file.readline().strip().split(' | ')
                ingredient_dict = {
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                }
                ingredients.append(ingredient_dict)
            cook_book[dish_name] = ingredients
            file.readline()
    return cook_book
file_name = 'recipes.txt'
cook_book = read_cook_book(file_name)
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else: 
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list  


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)