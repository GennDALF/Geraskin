# 141
# Несмотря на то что популярность оплаты по чекам за последние годы серьезно 
# снизилась, некоторые компании до сих пор используют этот способ для ведения 
# взаиморасчетов с сотрудниками и поставщиками. Сумма на чеках обычно указывается 
# дважды: один раз цифрами, второй – прописью на английском языке. Повторение суммы двумя
# разными формами записи призвано не позволить недобросовестным сотрудникам или поставщикам
# изменять сумму на чеках перед их обналичиванием. 
# В данном упражнении вам необходимо написать функцию, принимающую в качестве входного параметра 
# число от 0 до 999 и возвращающую строку прописью. Например, если значение параметра будет равно 142, 
# функция должна вернуть следующую строку: «one hundred forty two». Используйте один или несколько словарей 
# вместо условных конструкций if/elif/else для выработки решения этой задачи. Напишите основную 
# программу, в которой пользователь будет вводить числовое значение, а на 
# экран будет выводиться соответствующая сумма прописью.

value = int(input('please input a number\n'))

numbers = [{0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'},
{20: 'twenty', 30: 'thirty', 40: 'fourty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eightty', 90: 'ninety', 0: ''},
{100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred',
700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred', 0:''}, ]
exceptions = {11: 'eleven', 12: 'twelve', 13: 'thir-teen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
18: 'eighteen', 19: 'nineteen'}

def digit_change(value):
    res = []
    flag = True
    l = [(value % 10**(i+1)) // 10**i * 10**i for i in range(len(str(value)))]
    if 10 < l[0] + l[1] < 20:
        res = [exceptions[l[0] + l[1]]]
        flag = False
    r = range(len(l)) if flag else range(2, len(l))
    for i in r:
        res += [numbers[i][l[i]]]
    return res[::-1]
    
print(*digit_change(value))        


# C:\Users\Admin\Documents\python\Python\Homework\0405>py.exe Python115_Geraskin_2022_0405_task141.py
# please input a number
# 123
# one hundred twenty three

# C:\Users\Admin\Documents\python\Python\Homework\0405>py.exe Python115_Geraskin_2022_0405_task141.py
# please input a number
# 431
# four hundred thirty one



 