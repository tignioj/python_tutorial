def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


def test_func2(compute, **kwargs):
    x, y = kwargs['x'], kwargs['y']
    print(compute(x, y))


if __name__ == '__main__':
    test_func(compute)
    test_func2(compute, x=2, y=3)
