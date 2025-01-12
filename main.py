file = "recipes.txt"

def read_cookbook(file):
    cookbook = {}
    with open("recipes.txt", 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(f.readline().strip())
            ingredients = []
            for i in range(ingredients_count):
                ingredient_data = f.readline().strip().split(' | ')
                ingredient_name, quantity, measure = ingredient_data
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cookbook[dish_name] = ingredients
            f.readline()
    return cookbook

cook_book = read_cookbook(file)
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count, cookbook):
    shop_list = []
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if name not in shop_list:
                    shop_list[name] = {'measure' : measure, 'quantity' : quantity}
                else:
                    shop_list[name]['quantity'] += quantity
        else:
            print('Ошибка')
    return shop_list