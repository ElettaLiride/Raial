import functools


def tester(func):
    """Print if test is passed or not"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        if func(*args, **kwargs):
            print(f"Test: {func.__name__!r}  passed")
        else:
            print(f"Test: {func.__name__!r} failed")
    return wrapper_timer