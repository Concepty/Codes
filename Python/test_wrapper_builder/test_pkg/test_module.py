from common import wrapper_builder

__all__ = []
register = wrapper_builder(__all__)

@register
def test1():
    print('test1')

def test2():
    print('test2')