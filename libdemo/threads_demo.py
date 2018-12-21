import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(self.name, i)


print(threading.main_thread().name)
t = PrintThread()
t.name = "Child"
t.start()

t2 = PrintThread()
t2.name = "Child 2"
t2.start()

print("\nMain Done\n")
