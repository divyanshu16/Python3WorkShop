import time
import threading

mn = 2334
mm = []


def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square {}:{}'.format(mn, n*n))
        mm.append(n*n)


def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube {}: {}'.format(mn, n*n*n))
        mm.append(n*n*n)


def check_thread():
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def calc_sq_cu():
    calc_cube(arr)
    calc_cube(arr)


arr = [2, 3, 8, 9]

t = time.time()
# calc_sq_cu()
check_thread()
# print(mm)
print("done in : ", time.time()-t)