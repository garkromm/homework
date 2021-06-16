from contextlib import contextmanager
from functools import wraps


class ContextManagerNew():
    def __init__(self, f, *args, **kwargs):
        self.context = f(*args, **kwargs)

    def __enter__(self):
        return self.context

    def __exit__(self, exc_type, exc_value, traceback):
        print('I EXITED!')
        self.context.close()


def wrapped(f):
    def wrapper(func):
        func.__name__ = f.__name__
        func.__doc__ = f.__doc__
        return func
    return wrapper


def contextmanager_my_dec(f):
    @wrapped(f)
    def wrapper(*args, **kwargs):
        return ContextManagerNew(f, *args, **kwargs)
    return wrapper


@contextmanager_my_dec
def open_file(path, *args, **kwargs):
    file = open(path, *args, **kwargs)
    try:
        yield file
    finally:
        print('I EXITED TOO!')
        file.close()


def main():
    # file = ContextManagerNew( open,'text.txt', 'r' )
    # with file as f:
    #     for line in f:
    #         print(line)
    print(open_file.__name__)
    with open_file('text.txt') as f:
        for line in f:
            print(line)
    return 0


if __name__ == "__main__":
    main()
