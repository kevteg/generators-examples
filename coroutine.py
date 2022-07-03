

def coroutine():
    # dumb coroutine example
    x = 0
    while True:
        x = (yield x) + x
