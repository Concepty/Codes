In CPython implementation, any bytecode should get GIL to run. This means CPython guarantees each bytecode run in thread safe, but CPU bound tasks can not be efficiently distributed with python threads.


