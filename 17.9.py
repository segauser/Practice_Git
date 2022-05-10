"""
Напишите программу, которой на вход подается последовательность чисел через пробел,
а также запрашивается у пользователя любое число.
Далее программа работает по следующему алгоритму:
    1.Преобразование введённой последовательности в список
    2.Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
    3.Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за
    ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
Реализуйте его также отдельной функцией.
Подсказка:
    Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
    В этом случае необходимо вывести соответствующее сообщение
"""

# Тестовые данные
# array = '1 2 3 6 45 1 7 -95 4 5 1 8 9'
# array = '1 2 3 6 45 6 1 7 -95 4 6 5 1 6 8 9'
# array = '1 2 3 6 45 6 error 7 -95 4 6 5 1 6 8 9'
# array = '1 2 3 6 45 6 1 7 -95 4 6 5 1 6 8 9'
# element = 7
# element = 6
# array = list(array.split())


array = None
element = None
while True:
    while True:
        try:
            array = input('Введите последовательность чисел через пробел: ')
            array = list(array.split())
            for i in array:
                if int(i) == 0:
                    continue
                elif not int(i):
                    raise ValueError
            break
        except ValueError as error:
            print('В вашей последовательности недопустимые значения')
    while True:
        try:
            element = int(input('Введите искомое число: '))
            break
        except ValueError as error:
            print('Вы ввели не число')
    if (array and element) or (array and element==0):
        break


def sort(arr):
    list = []
    for i in arr:
        list.append(int(i))
    list.sort()
    return list

# Алгоритм не совершенен, при попытке возвратить индекс числа из неуникального массива
def position_number(array, element, left, right):  # Алгоритм двоичного поиска
    if element > sort_arr[-1]:  # Чтобы убрать IndexError при element>sort_arr[-1] не вызывая исключение
        return False
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return position_number(array, element, left, middle - 1)
    else:  # иначе в правой
        return position_number(array, element, middle + 1, right)


sort_arr = sort(array)
print('Отсортированный массив: ', sort_arr)
print('Искомое число: ', element)

pos_num = position_number(sort_arr, element, 0, len(sort_arr))
print('Индекс искомого числа через алгоритм бинарного поиска:', pos_num)  # индекс искомого
# print('Индекс методом .index():', sort_arr.index(element)) # При element>sort_arr[-1] IndexError

if sort_arr[pos_num - 1] < element and sort_arr[-1] == element:  # Правая граница
    print(f'Число меньше искомого пользователем: {sort_arr[pos_num - 1]}')
    print(f'Большего числа не существует')
elif sort_arr[0] == element and len(sort_arr)==1:
    print(f'Ваше число: {element}, Чисел больше или меньше вашего в массиве не существует.')
elif sort_arr[0] == element and sort_arr[pos_num + 1] >= element:  # Левая граница
    print(f'Число больше или равно искомого пользователем: {sort_arr[pos_num + 1]}')
    print(f'Меньшего числа не существует')
elif sort_arr[0] < element and len(sort_arr) == 1: # Для element > единственного числа массива, убрать IndexError
    print(f'Искомое число больше последнего числа массива')
    print(f'Ближайшее меньшее число: {sort_arr[0]}')
elif sort_arr[pos_num - 1] < element and sort_arr[pos_num + 1] >= element:  # Существующее число в диапазоне массива
    print(f'Число меньше искомого пользователем: {sort_arr[pos_num - 1]}')
    print(f'Число больше или равно искомому пользователем: {sort_arr[pos_num + 1]}')
else:
    if element in list(range(sort_arr[0], sort_arr[-1] + 1)):  # Число в диапозоне массива, но нет среди чисел массива
        for i in list(range(len(sort_arr))):
            if sort_arr[i] < element and sort_arr[i+1]> element:
                print(f'Ближайшее меньшее число: {sort_arr[i]}')
                print(f'Ближайшее большее число: {sort_arr[i+1]}')
    elif element not in list(range(sort_arr[0], sort_arr[-1] + 1)) and element > sort_arr[-1]:  # Больше верхней границы
        print(f'Искомое число больше последнего числа массива')
        print(f'Ближайшее меньшее число: {sort_arr[-1]}')
    elif element not in list(range(sort_arr[0], sort_arr[-1] + 1)) and element < sort_arr[0]:  # Меньше нижней границы
        print(f'Искомое число меньше первого числа массива')
        print(f'Ближайшее большее число: {sort_arr[0]}')
