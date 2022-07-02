# Python - Async
This was the second project in the alx/holberton software engineering backend-python curriculum. In this project I learned about coroutines.

[asyncio]('https://docs.python.org/3/library/asyncio.html') is a library to write concurrent code using the async/await syntax. asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
asyncio is often a perfect fit for IO-bound and high-level structured network code.


During this project I learnt the following:
- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Running the programs
To test the functions make sure the main.py files are in the same directory as the specific task files and run the following command:
**./<num>-main.py**

## Tasks:
### 0. The basics of Async

**File:**

[0-basic_async_syntax.py](./0-basic_async_syntax.py): Defines an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
- Generate a Random floating point number using:

**random.uniform(start, stop)**

### 1. Let's execute multiple coroutines at the same time with async

**File:**

[1-concurrent_coroutines.py](./1-concurrent_coroutines.py): Imports the __wait_random__ coroutine from the [0-basic_async_syntax.py](./0-basic_async_syntax.py) file and defines an async routine called __wait_n__ that takes in 2 int arguments (in this order): n and max_delay.
- spawn wait_random n times with the specified max_delay.
- wait_n should return the list of all the delays (float values).
- The list of the delays should be in ascending order without using sort() because of concurrency.

### 2. Measure the runtime

**File:**

[2-measure_runtime.py](./2-measure_runtime.py): Measures the total execution time for wait_n(n, max_delay),\
* and returns total_time / n.
* The function returns a float
* Uses the time module to measure an aproximate elapsed time.

### 3. Tasks

**File:**

**Tasks** are used to schedule coroutines concurrently.
When a coroutine is wrapped into a Task with functions like _asyncio.create_task()_ the coroutine is automatically scheduled to run soon.

*File:*

[3-tasks](./3-tasks): Implements a regular function (task_wait_random) that takes an integer max_delay and returns a asyncio.Task.

### 4. Tasks

In this task I created a function that runs the task_wait_random function.

**File:**

[4-tasks](./4-tasks): Modifies the wait_n to task_wait_n function.
