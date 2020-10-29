def print_result(func_to_decorate):

    def decorated_func(*arg):
        print(func_to_decorate.__name__)
        a = func_to_decorate(*arg)
        if type(a) is list:
            for i in a:
                print(i)
        elif type(a) is dict:
            for key in a:
                print("{} = {}".format(key, a[key]))
        else:
            print(a)
        return a
    return decorated_func

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]