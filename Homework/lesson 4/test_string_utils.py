import pytest
from string_utils import StringUtils 

string_utils = StringUtils()

#Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
@pytest.mark.parametrize( "inputWord, result", [ 
    # позитивный сценарий
    ("skypro", "Skypro"),
    ("House", "House"),
    ("two words", "Two words"),
    ("", ""),
    ("AHHHHH", "Ahhhhh"), 
    # негативный сценарий 
    (pytest.param(123, "", marks=pytest.mark.xfail)), # проверка поля на ввод цифр. 
    (pytest.param("   ", "   ", marks=pytest.mark.xfail)), # не должно принимать только одни пробелы. либо должно возвращать пустое поле. Нужно уточнить. 
    (pytest.param(None, "", marks=pytest.mark.xfail)),  # Входное значение None, ожидаемый результат пустая строка
])
def test_Capitilize(inputWord, result):
    string_utils = StringUtils() 
    res = string_utils.capitilize(inputWord)
    assert res == result

#Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.mark.parametrize( "inputWord, result", [ 
    # позитивный сценарий
    ("House", "House"),
    ("   123", "123"),
    ("    ", ""),
    # негативный сценарий 
    (pytest.param(123, "", marks=pytest.mark.xfail)), # проверка поля на ввод цифр. 
    (pytest.param("  two   words   ", "two words   ", marks=pytest.mark.xfail)), # Удаление пробелов после слова. Уточнение по ТЗ
    (pytest.param("  two   words", "two words", marks=pytest.mark.xfail)), # удаление пробелов между словами
    (pytest.param(None, "", marks=pytest.mark.xfail)),  # Входное значение None, ожидаемый результат пустая строка
])
def test_Trim(inputWord, result):
    string_utils = StringUtils()
    res = string_utils.trim(inputWord)
    assert res == result

# Принимает на вход текст с разделителем и возвращает список строк.
@pytest.mark.parametrize( "inputWord, delimeter, result", [ 
    # позитивный сценарий
    ("a,b,c,d",",", ["a", "b", "c", "d"]),
    ("a:b:c:d",":", ["a", "b", "c", "d"]),
    ("1:2:3",":", ["1", "2", "3"]),
    (" ",",",[]),
    ("a",",",["a"])
] )
def test_PositiveTo_list(inputWord, delimeter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(inputWord, delimeter)
    assert res == result

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
@pytest.mark.parametrize( "inputWord, symbol, result", [
    # позитивный сценарий
    ("SkyPro", "S", True),
    ("Cat", "a", True),
    ("SkyPro", "o", True),
    ("SkyPro", "z", False),
    ("", "A", False), 
    # негативный сценарий
    (pytest.param("Hello", "", False, marks=pytest.mark.xfail)), # Негативная проверка: пустая строка не содержит ничего
    (pytest.param(None, "A", False, marks=pytest.mark.xfail)), # Негативная проверка: при передаче None функция должна вернуть False
    (pytest.param("Hello", None, False, marks=pytest.mark.xfail)), # Негативная проверка: при передаче None в качестве символа функция должна вернуть False
    (pytest.param(None, None, False, marks=pytest.mark.xfail)), # Негативная проверка: при передаче двух None функция должна вернуть False
])
# Удаляет все подстроки из переданной строки
def test_PositiveContains(inputWord, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(inputWord, symbol)
    assert res == result

@pytest.mark.parametrize( "inputWord, symbol, result", [
    # позитивный сценарий
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "", ""),
    ("", "A", ""),
    ("Cat", "", "Cat"),
    # негативный сценарий
    ("Hello", "x", "Hello"),
    (pytest.param(None, "A", None, marks=pytest.mark.xfail)), #  передаем None в качестве строки, она должна остаться неизменной
    (pytest.param("Hello", None, "Hello", marks=pytest.mark.xfail)), #  передаем None в качестве символа, строка остается неизменной
    (pytest.param(None, None, None, marks=pytest.mark.xfail)) #  передаем два None, возвращаем None
])
def test_delete_symbol(inputWord, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(inputWord, symbol)
    assert res == result

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
@pytest.mark.parametrize( "inputWord, symbol, result", [
    # позитивный сценарий
    ("SkyPro", "S", True),
    ("Cat", "C", True),
    ("SkyPro", "K", False),
    ("SkyPro", "P", False),
    ("", "", True),
    ("Python", "Py", True),  
    # негативный сценарий
    ("SkyPro", "z", False),
    (pytest.param("", "A", False, marks=pytest.mark.xfail)), #пустая строка не начинается с символа "A"
    (pytest.param(None, "A", False, marks=pytest.mark.xfail)), # передаем None в качестве строки, она не начинается с символа "A"
    (pytest.param("Hello", None, False, marks=pytest.mark.xfail)), # передаем None в качестве символа, строка не начинается с None
    (pytest.param(None, None, None, marks=pytest.mark.xfail)) #  передаем два None, возвращаем None
])

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
def test_starts_with(inputWord, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(inputWord, symbol)
    assert res == result

@pytest.mark.parametrize( "inputWord, symbol, result", [
    # позитивный сценарий
    ("SkyPro", "o", True),
    ("Cat", "t", True),
    ("SkyPro", "r", False),
    ("", "", True), 
    ("Test", "st", True),
    # негативный сценарий
    ("SkyPro", "z", False),
    (pytest.param("", "A", False, marks=pytest.mark.xfail)), #пустая строка не начинается с символа "A"
    (pytest.param(None, "A", False, marks=pytest.mark.xfail)), # передаем None в качестве строки, она не начинается с символа "A"
    (pytest.param("Hello", None, False, marks=pytest.mark.xfail)), # передаем None в качестве символа, строка не начинается с None
    (pytest.param(None, None, None, marks=pytest.mark.xfail)) #  передаем два None, возвращаем None
])
def test_end_with(inputWord, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(inputWord, symbol)
    assert res == result

# Возвращает `True`, если строка пустая и `False` - если нет
@pytest.mark.parametrize( "inputWord,result", [
    # позитивный сценарий
    ("", True),  
    ("  ", True),
     (pytest.param(None, True, marks=pytest.mark.xfail)), # ошибка, None  это так же пустая строка. 
    # негативный сценарий 
    ("SkyPro",False),
    ("0", False),
    (".", False),
])
def test_is_empty(inputWord,result):
    string_utils = StringUtils()
    res = string_utils.is_empty(inputWord)
    assert res == result

# Преобразует список элементов в строку с указанным разделителем
@pytest.mark.parametrize( "lst, joiner, result", [
    ([1,2,3,4], ", ", "1, 2, 3, 4"),
    ([], ", ", ""),
    ([0], ", ", "0")
])
def test_list_to_string(lst, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(lst, joiner)
    assert res == result

