"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    to_str = str(ticket_num)
    to_list = list(to_str)
    lentgh_list = len(to_list)
    half_1 = half_2 = 0
    for i in range(lentgh_list):
        if i < lentgh_list // 2:
            half_1 += int(to_list[i])
        else:
            half_2 += int(to_list[i])
    if half_1 == half_2:
        return True
    else:
        return False


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")
