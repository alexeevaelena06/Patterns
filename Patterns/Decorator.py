"""Декоратор - паттерн проектирования.
Декораторы позволяют динамически изменять поведение или расширять функциональность существующих
функций без изменения самой функции."""


def make_string_upper(func):
    def inner(string):
        func(string.upper())
    inner.__name__ = func.__name__
    return inner


@make_string_upper
def my_func(*arg, **kwargs):
    print(*arg, **kwargs)


if __name__ == '__main__':
    my_func("jam")
    my_func("egg")
    print(my_func.__name__)





