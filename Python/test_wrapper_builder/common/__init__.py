import inspect
import functools

def wrapper_builder(all):
    def w(f):
        all.append(f.__name__)
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return w