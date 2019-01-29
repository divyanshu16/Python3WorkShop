import time
import multiprocessing

outside_results = []


def calc_square(numbers):
    for n in numbers:
        print('square of {} : {}'.format(n, n*n))
    #     outside_results.append(n*n)
    # print(outside_results)


def calc_cube(numbers):
    for n in numbers:
        print('cube of {} : {}'.format(n, n*n*n))


def check_processes_1():
    arr = [2, 3, 8, 9]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(outside_results)


def check_processes_2():
    def calc_square_mp(numbers, result, v):
        for idx, n in enumerate(numbers):
            result[idx] = n * n
            v.value += 1

    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square_mp, args=(numbers, result, v))

    p.start()
    p.join()

    print(v.value)
    print(result[:])


def check_no_lock():

    def deposit(balance):
        for i in range(100):
            time.sleep(0.01)
            balance.value = balance.value + 1

    def withdraw(balance):
        for i in range(100):
            time.sleep(0.01)
            balance.value = balance.value - 1

    if __name__ == '__main__':
        balance = multiprocessing.Value('i', 200)
        d = multiprocessing.Process(target=deposit, args=(balance, ))
        w = multiprocessing.Process(target=withdraw, args=(balance, ))
        d.start()
        w.start()
        d.join()
        w.join()
        print(balance.value)


def check_lock():

    def deposit(balance, lock):
        for i in range(100):
            time.sleep(0.01)
            lock.acquire()
            balance.value = balance.value + 1
            lock.release()

    def withdraw(balance, lock):
        for i in range(100):
            time.sleep(0.01)
            lock.acquire()
            balance.value = balance.value - 1
            lock.release()

    if __name__ == '__main__':
        balance = multiprocessing.Value('i', 200)
        lock = multiprocessing.Lock()
        d = multiprocessing.Process(target=deposit, args=(balance, lock))
        w = multiprocessing.Process(target=withdraw, args=(balance, lock))
        d.start()
        w.start()
        d.join()
        w.join()
        print(balance.value)


if __name__ == "__main__":
    t0 = time.time()
    # check_processes_1()
    # check_processes_2()
    # check_no_lock()
    check_lock()
    print("done in : ", time.time() - t0)
    print("Done!")