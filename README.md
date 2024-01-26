This async example is inspired by the <a href="https://fastapi.tiangolo.com/async/#concurrent-burgers" class="external-link" target="_blank">Concurrency and Burgers</a> example.

Things to note:

- The `async` keyword is used to define an asynchronous function.
- The `await` keyword is used to call an asynchronous function.
- If you need to `await` for a function call, the calling function must be `async` (async def).
- If you want to call an asynchronous function from a synchronous function, you can use `asyncio.run()`.

There are basically two ways to run asynchronous functions:

```python
async def some_async_function():
    tasks = asyncio.gather(coroutine1(), coroutine2(), coroutine3())
    await tasks
```

or

```python
async def some_async_function():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    task3 = asyncio.create_task(coroutine3())
    await task1
    await task2
    await task3
```

and then you can call the asynchronous function from a synchronous function:

```python
def some_sync_function():
    asyncio.run(some_async_function())
```
