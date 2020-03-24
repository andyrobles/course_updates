
from threading import Thread
import time

class FunctionLoop:
    def function(self):
        print('Function call')

    def function_loop(self, function):
        while True:
            function()
            time.sleep(1)

    def execute(self):
        Thread(target=self.function_loop, args=(self.function,)).start()