# single_threaded.py
import time
from threading import Thread


def countdown(n):
    while n > 0:
        n -= 1


def simple_countdown():
    # CPU intensive task
    COUNT = 50000000
    countdown(COUNT)


def time_wait(n):
    # I/O bound task
    time.sleep(n)


def simple_wait():
    COUNT = 10
    time_wait(COUNT)


def threaded_countdown():
    """
     In the multi-threaded version the GIL prevented the CPU-bound threads from executing in parellel.

     program whose threads are entirely CPU-bound,
     e.g., a program that processes an image in parts using threads, would not only become single threaded due to the
     lock but will also see an increase in execution time, as seen in the above example,
     in comparison to a scenario where it was written to be entirely single-threaded.
     This increase is the result of acquire and release overheads added by the lock.
    """
    COUNT = 50000000
    t1 = Thread(target=countdown, args=(COUNT // 2,))
    t2 = Thread(target=countdown, args=(COUNT // 2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


def threaded_io():
    """
    The GIL does not have much impact on the performance of I/O-bound multi-threaded programs
    as the lock is shared between threads while they are waiting for I/O.
    """
    COUNT = 10
    t1 = Thread(target=time_wait, args=(COUNT // 2,))
    t2 = Thread(target=time_wait, args=(COUNT // 2,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


start = time.time()
# simple_countdown()
# threaded_countdown()

# simple_wait()
threaded_io()
end = time.time()

print('Time taken in seconds -', end - start)