import inspect
import functools

def register_to_all(f):
    print('registering...')
    f_module = inspect.getmodule(inspect.stack()[1][0])
    try:
        all_obj = inspect.getattr_static(f_module, '__all__')
        all_obj.append(f.__name__)
    except AttributeError as AE:
        print(f'__all__ does not exist in the module {f_module.__name__}')
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper