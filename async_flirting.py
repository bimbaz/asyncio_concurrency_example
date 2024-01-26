import asyncio
import time


async def cook_burger():
    steps = [
        "cook patty",
        "add cheese",
        "add tomato",
        "add condiments",
        "wrap burger",
    ]
    for step in steps:
        print(f"kitchen: {step}")
        await asyncio.sleep(1)
    print("kitchen: burger is ready")


async def flirting():
    steps = [
        "make eye contact",
        "smile",
        "say hello",
        "say something funny",
        "say something interesting",
        "ask what they do for fun",
        "ask what is their favorite food",
        "ask what is their favorite movie",
        "ask what is their favorite song",
    ]
    for step in steps:
        print(f"date: {step}")
        await asyncio.sleep(1)
    print("date: you got a date")


async def go_date():
    print("start async date")
    print("go to restaurant")
    print("order burger")
    tasks = asyncio.gather(cook_burger(), flirting())
    await tasks


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(go_date())
    print("total time: ", time.time() - start_time)
