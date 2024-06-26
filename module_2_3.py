task = 'Домашняя работа по уроку "Стиль кода часть II. Цикл While."'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(f'Список: {my_list}')
print(f'Число элементов в списке: {len(my_list)}')
print()
print('1. Список остановится когда встретится отрицательное число.')
counter = 0
counter_a = len(my_list)
while counter < counter_a:
    counter_b = my_list[counter]
    counter = counter + 1
    if counter_b == 0:
        continue
    elif counter_b > 0:
        print('Положительное число:', counter_b)
        continue
    else:
        print('"Stop!", на пути отрицательное число.')
        break
print()
print('2. Список пролистается до конца убрав отрицательные числа и нули.')
counter = 0
while counter < counter_a:
    counter_b = my_list[counter]
    counter = counter + 1
    if counter_b == 0:
        continue
    elif counter_b > 0:
        print('Положительное число:', counter_b)
print()
print(thanks)