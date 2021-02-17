"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.
    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""

""" Функция возвращает список самых длинных строк из списка list_in """
def longest_strings(list_in):
#    t_1 = ["x"]
#    max(t_1, key=len)
#    return t_1
    t_2 = ["abc", "eeee", "abcd", "dcd"]
#    length = max(t_2, key=len)
#    print(length)
    str_list = [x for x in t_2 if isinstance(x, str)]
    longestword = sorted(str_list, key=len, reverse=True)[0]
    print(longestword)


#t_1 = ["x"]
#assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]
'''
t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]
'''
print("All tests passed successfully!")
