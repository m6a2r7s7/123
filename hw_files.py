from pprint import pprint
#задача 1
def recipes_reader(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as file_obj:
        dict_recipes = {}
        for line in file_obj:
            dish_name = line.strip()
            dict_recipes[dish_name] = []
            quantity = file_obj.readline().strip()
            for item in range (int(quantity.strip())):
                ingredient = {}
                obj = file_obj.readline()
                obj = obj.strip().replace('|', '')
                obj = obj.split()
                if len(obj) == 3:
                    ingredient['ingredient_name'] = obj[0]
                    ingredient['quantity'] = int(obj[1])
                    ingredient['measure'] = obj[2]
                else:
                    ingredient['ingredient_name'] = obj[0] + ' ' + obj[1]
                    ingredient['quantity'] = int(obj[2])
                    ingredient['measure'] = obj[3]
                dict_recipes[dish_name].append(ingredient)
            file_obj.readline()
        return dict_recipes
pprint(recipes_reader('recipes.txt'))
#задача 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_cook = recipes_reader('recipes.txt')
    result = {}
    for dish in dishes:
        for target_dish in cook_cook:
            if dish == target_dish:
                for ingredient in cook_cook[target_dish]:
                    res = {}
                    res['measure'] = ingredient['measure']
                    res['quantity'] = (ingredient['quantity'] * person_count)
                    result[ingredient['ingredient_name']] = res

            else:
                None
        for i in range(len(dishes)):
            if (len(dishes) > 1) and (dishes[i] == dishes[i + 1]):
                for item in result:
                    result[item]['quantity'] *= 2
                return result
            else:
                None
    return result
pprint(get_shop_list_by_dishes(['Омлет'], 2))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
# задача 3
def merging_files(file_1, file_2, file_3):
    result = ''
    with open(file_1, encoding='utf-8') as file_obj_1:
        with open(file_2, encoding='utf-8') as file_obj_2:
            with open(file_3, encoding='utf-8') as file_obj_3:
                file1 = file_obj_1.read()
                file2 = file_obj_2.read()
                file3 = file_obj_3.read()
                def num_of_lines(file):
                    num = file.count('\n')
                    if num > 1:
                        num += 1
                    else:
                        num = 1
                    return num
                files_dict = {file_obj_1:
                                  {'text': file1, 'length': num_of_lines(file1)},
                              file_obj_2:
                                  {'text': file2, 'length': num_of_lines(file2)},
                              file_obj_3:
                                  {'text': file3, 'length': num_of_lines(file3)}
                              }
                files_length = [files_dict[file_obj_1]['length'], files_dict[file_obj_2]['length'], files_dict[file_obj_3]['length']]
                files_length.sort()
                result = ''
                for num in range(len(files_length)):
                    for file in files_dict:
                        if files_length[num] == files_dict[file]['length']:
                            result = result + str(file.name) + '\n' + str(files_dict[file]['length']) + '\n' + files_dict[file]['text'] + '\n'
                        else:
                            None
                return result

print(merging_files('1.txt', '2.txt', '3.txt'))








