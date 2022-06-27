# Python - Async
## Learning Objectives

- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module


## Tasks:
* **0. The basics of Async**
[0-basic_async_syntax.py](./0-basic_async_syntax.py): Defines an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
- Generate a Random floating point number using:
**random.uniform(start, stop)**

* **1. Let's execute multiple coroutines at the same time with async**
[1-concurrent_coroutines.py](./1-concurrent_coroutines.py): Imports the __wait_random__ coroutine from the [0-basic_async_syntax.py](./0-basic_async_syntax.py) file and defines an async routine called __wait_n__
that takes in 2 int arguments (in this order): n and max_delay.
- spawn wait_random n times with the specified max_delay.
- wait_n should return the list of all the delays (float values).
- The list of the delays should be in ascending order without using sort() because of concurrency.