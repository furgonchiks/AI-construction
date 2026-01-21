# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(grupp1, grupp2, arg=','):
    list1 = grupp1.split(arg)
    list2 = grupp2.split(arg)

    common = list(set(list1) & set(list2))
    common.sort()
    return common
grupp1 = "Иванов,Петров,Сидоров"
grupp2 = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result = find_common_participants(grupp1, grupp2)
print("Общие участники:", result)

