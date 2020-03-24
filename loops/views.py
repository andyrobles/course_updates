from threading import Thread
import time

def function():
    print('Function call')

def function_loop(function):
    while True:
        function()
        time.sleep(1)

Thread(target=function_loop, args=(function,)).start()