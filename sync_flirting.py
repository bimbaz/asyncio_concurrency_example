import time


def cook_burger():
    steps = [
        "cook patty",
        "add cheese",
        "add tomato",
        "add condiments",
        "wrap burger",
    ]
    for step in steps:
        print(f"kitchen: {step}")
        time.sleep(1)
    print("kitchen: burger is ready")


def flirting():
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
        time.sleep(1)
    print("date: you got a date")


def go_date():
    print("start sync date")
    print("go to restaurant")
    print("order burger")
    cook_burger()
    flirting()


if __name__ == "__main__":
    start_time = time.time()
    go_date()
    print("total time: ", time.time() - start_time)
