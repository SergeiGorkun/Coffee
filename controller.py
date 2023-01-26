
def coffee_making(coffee_name, ingridients):
    status = True;
    if coffee_name == 'Эспрессо':
        if ingridients['coffee_bean'] >= 1:
            ingridients['coffee_bean'] -= 1
        else:
            status = False    
    elif coffee_name == 'Капуччино':
        if ingridients['coffee_bean'] >= 1 and ingridients['milk'] >= 3:
            ingridients['coffee_bean'] -= 1
            ingridients['milk'] -= 3
        else:
            status = False
    elif coffee_name == 'Маккиато':
        if ingridients['coffee_bean'] >= 2 and ingridients['milk'] >= 1:
            ingridients['coffee_bean'] -= 2
            ingridients['milk'] -= 1
        else:
            status = False   
    elif coffee_name == 'Кофе по-венски':
        if ingridients['coffee_bean'] >= 1 and ingridients['whipped_cream'] >= 2:
            ingridients['coffee_bean'] -= 1
            ingridients['whipped_cream'] -= 2
        else:
            status = False   
    elif coffee_name == 'Латте Маккиато':
        if ingridients['coffee_bean'] >= 1 and ingridients['milk'] >=2 and ingridients['whipped_cream'] >= 1:
            ingridients['coffee_bean'] -= 1
            ingridients['milk'] -= 2
            ingridients['whipped_cream'] -= 1
        else:
            status = False   
    elif coffee_name == 'Кон Панна':
        if ingridients['coffee_bean'] >= 1 and ingridients['whipped_cream'] >= 1:
            ingridients['coffee_bean'] -= 1
            ingridients['whipped_cream'] -= 1
        else:
            status = False  
    else:
        print('К сожалению, не можем Вам предложить ' + coffee_name)
        return {
            'status': False,
            'ingridients': ingridients
        }
        
    return {
        'status': status,
        'ingridients': ingridients
    }
