"""Дано дробное число в двоичной системе счисления, т.е. последовательность цифр 0 и 1, разделенных точкой.
Составить программу перевода этого числа в восьмеричную систему счисления."""

"""Функция для записи в массивы дробного двоичного числа в два массива до и после точки """
bin_code_str = str(input("Введите дробное двоичное число через точку: "))
len_bin_before = 0
for i in range(len(bin_code_str)):
    if bin_code_str[i] == ".":
        len_bin_before = i

len_bin_after = len(bin_code_str) - len_bin_before - 1

bin_code_before = [0] * len_bin_before
bin_code_after = [0] * len_bin_after

for i in range(len_bin_before):
    bin_code_before[i] = int(bin_code_str[i])

for i in range(len_bin_after):
    bin_code_after[i] = int(bin_code_str[i+len_bin_before+1])

#print("Цифры перед точкой: ", bin_code_before)
#print("Цифры после точки: ", bin_code_after)
"""----------------------------------------------------------------------------------"""


"Перевод из двоичной в десятичную"


def to_ten(bin_before, bin_after):

    bin_before = bin_before[::-1]
    bin_after = bin_after[::-1]

    dec_before = 0.0
    dec_after = 0.0

    for i in range(0, len_bin_before):
        dec_before += bin_before[i] * pow(2, i)

    for i in range(-1*len_bin_after, 0):
        dec_after += bin_after[i] * pow(2, i)

    dec = dec_after + dec_before

    return dec


def to_eight(dec_before, dec_after):
    count_before = 0
    count_after = 0

    dec_before_clone = dec_before
    g = dec_after
    dec_after = dec_after * pow(10, (-1*len_dec_after))
    dec_after_clone = dec_after

    l = 8

    while dec_before > 0:
        dec_before = dec_before // 8
        count_before += 1

    while g != 0:
        dec_after = dec_after * 8
        g = dec_after - int(dec_after)
        count_after += 1

    dec_before_list = [0] * count_before
    dec_after_list = [0] * count_after
    i = 0

    while dec_before_clone != 0:
        dec_before_list[i] = dec_before_clone % 8
        dec_before_clone = dec_before_clone // 8
        dec_before_list[i] = str(dec_before_list[i])
        i += 1

    i = 0

    while l != 0:
        dec_after_clone *= 8
        l = dec_after_clone - int(dec_after_clone)
        dec_after_list[i] = int(dec_after_clone)
        dec_after_list[i] = str(dec_after_list[i])
        i += 1

    dec_before_list = dec_before_list[::-1]
    dec_after_list = dec_after_list[::-1]

    dec_code_before = ""
    dec_code_after = ""

    for i in range(count_before):
        dec_code_before += dec_before_list[i]

    for i in range(count_after):
        dec_code_after += dec_after_list[i]

    dec = int(dec_code_before) + \
        (int(dec_code_after) * pow(10, -1*count_after))
    return dec


"""Функция записи дробного десятичного числа в 2 массива до и после точки"""
dec_code_str = str(to_ten(bin_code_before, bin_code_after)
                   )  # получение десятичного числа в строке
print("Десятичное число: ", dec_code_str)
len_dec_before = 0

for i in range(len(dec_code_str)):
    if dec_code_str[i] == ".":
        len_dec_before = i
len_dec_after = len(dec_code_str) - len_dec_before - 1


if len_dec_after > 3:
    print("ВНИМАНИЕ, есть шанс того что восьмеричное представление числа может быть неправильно \nиз-за особенностей ЯП Питон в работе цифрами после запятой \n")


dec_code_before = ""
dec_code_after = ""

for i in range(len_dec_before):
    dec_code_before += dec_code_str[i]

for i in range(len_dec_after):
    dec_code_after += dec_code_str[i+len_dec_before+1]

dec_code_before = int(dec_code_before)
dec_code_after = int(dec_code_after)

#print("Число перед точкой: ", dec_code_before)
#print("Число после точки: ", dec_code_after)

"""------------------------------------------------------------------"""
print("Восьмеричное число: ", to_eight(dec_code_before, dec_code_after))

input()