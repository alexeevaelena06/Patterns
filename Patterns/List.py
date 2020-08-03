

def foo(a=None):
    print(type(a))
    print(id(a))
    if a is None:
        a = []
    a.append(1)
    print(type(a))
    print(id(a))
    print(a)

b = [23]

if __name__ == '__main__':
    foo()
    foo()
    foo(b)
    print(b)