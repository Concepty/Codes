from test_wrapper import register_to_all

__all__ = []

@register_to_all
def test():
    print('test called')