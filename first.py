import time


def fib():
    '''Old friend fibo <3'''
    a, b = 0, 1
    while True:
       yield b
       # Sleep to be able to see the numbers generation
       time.sleep(1)
       a, b = b, a+b

