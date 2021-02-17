"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""


def is_lucky(ticket_num):
    s = str(ticket_num)
    x = list(s)
    lentgh_list = len(x)
    s1 = s2 = 0
    for i in range(lentgh_list):
        if i < lentgh_list // 2:
            s1 += int(x[i])
        else:
            s2 += int(x[i])
    if s1 == s2:
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
