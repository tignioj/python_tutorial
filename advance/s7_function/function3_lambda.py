def test_func(compute):
    result = compute(1, 2)
    print(result)


def test_func2(compute, **kwargs):
    x, y = kwargs['x'], kwargs['y']
    print(compute(x, y))


if __name__ == '__main__':
    test_func(lambda x, y: x + y)
    test_func2(lambda x, y: x + y, x=2,y=3)
