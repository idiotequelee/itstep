'''
Напишіть програму shopping_ultra.py, 
що буде надавати можливість додавати нові списки, 
видаляти вже існуючі, знаходити найдорожчий і найдешевший 
список з покупками, зчитувати дані при першому вході з файлу 
(де дані серіалізовані) та після завершення роботи 
серіалізувати та зберігати у файл (формат серіалізації json). 
'''



import json 

def welcome_message():
    while True:
        print("\n1 - viev my shopping list")
        print("2 - add purchases")
        print("3 - delete purchases")
        print("4 - find the most expensive list")
        print("5 - find the cheapest list")
        print("6 - exit")

        user_input = int(input("\nEnter what you to do "))
        if user_input == 1:
            viev_list(open_json())
        elif user_input == 2:
            add_purchases()
        elif user_input == 3:
            delete_purchases()
        elif user_input == 4:
            find_expensive()
        elif user_input == 5:
            find_cheapest()
        elif user_input == 6:
            break
        else:
            print("\nPlease, enter the options from 1 to 6")


def open_json():
    with open("shopping_list.json") as json_file:
        data = json.load(json_file)
    return data


def save_json(data):
    with open("shopping_list.json", 'w') as data_file:
        json.dump(data, data_file, indent=2)



def viev_list(data):
    index = 0
    for item in data:
        print(f"\nlist # {index}")
        print(item)
        index +=1


def add_purchases():
    shopping_list = open_json()
    item = input("\nEnter name of item ")
    cost_of_item = int(input("Enter cost of item "))
    shopping_list.append([{item: cost_of_item}])
    save_json(shopping_list)


def delete_purchases():
    viev_list(open_json())
    new_list = []
    data = open_json()
    list_size = len(data)-1
    index = 0
    delete_option = input(f"\nWhat list do you want to delete? \nChoose the number from 0 to {list_size}: ")
    for item in data:
        if index == int(delete_option):
            pass
            index += 1
        else:
            new_list.append(item)
            index += 1
    save_json(new_list)


def find_expensive():
    viev_list(open_json())
    data = open_json()
    value_list = []
    for item in data:
        list_sum = sum(item.values())
        value_list.append(list_sum)
        max_value = max(value_list)
    max_index = (value_list.index(max_value))
    print(f"\nThe most expensive is list # {max_index} with costs {max_value} \n{value_list}")


def find_cheapest():
    viev_list(open_json())
    data = open_json()
    value_list = []
    for item in data:
        list_sum = sum(item.values())
        value_list.append(list_sum)
        min_value = min(value_list)
    min_index = (value_list.index(min_value))
    print(f"\nThe cheapest is list # {min_index} with costs {min_value} \n{value_list}")


welcome_message()
            
            

