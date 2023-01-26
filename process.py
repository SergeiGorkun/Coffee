import controller

def choose_coffee(*preferences):

    ingridients = {
        'coffee_bean': int(input('Введите количество порции кофейных зёрен: ')),
        'milk': int(input('Введите количество порции молока ')),
        'whipped_cream': int(input('Введите количество порции взбитых сливок: ')),
    }
    for coffee_name in preferences:
        while True:
            res = controller.coffee_making(coffee_name, ingridients)
            ingridients = res['ingridients']
            if res['status'] == False:
                break
            else:
                print('Ваш кофе ' + coffee_name + ' готов!')     
