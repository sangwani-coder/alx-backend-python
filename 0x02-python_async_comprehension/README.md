# 0x02-python_async_comprehension
Python 3.6 added the ability to create Asynchronous Comprehensions and Asynchronous Generators. You can read about asynchronous comprehension in
[PEP 530](https://peps.python.org/pep-0530/) while the asynchronous generators are described in [PEP 525](https://peps.python.org/pep-0525/). The documentation states that you can now create asynchronous list, set and dict comprehensions and generator expressions.
Their example looks like this:
**result = [i async for i in aiter() if i % 2]**

## Task Files:
* [x] [0-async_generator.py](./0-async_generator.py)
* [x] [1-async_comprehension.py](./1-async_comprehension.py)
* [x] [2-measure_runtime.py](./2-measure_runtime.py)
