import ctypes
import sys


def simple_refcount():
    """
    Examples, where the reference count increases:
    assignment operator
    argument passing
    appending an object to a list (object's reference count will be increased).
    """

    foo = []

    # 2 references, 1 from the foo var and 1 from getrefcount
    print(sys.getrefcount(foo))

    def bar(a):
        # 4 references
        print(sys.getrefcount(a))

    bar(foo)
    # 2 references, the function scope is destroyed
    print(sys.getrefcount(foo))

    print(id(foo))
    foo = "fdjsndsf"
    print(sys.getrefcount(foo))
    print(id(foo))


def ggc():

    """
    Generational garbage collector : circular references

    The reference counting module is fundamental to Python and can't be disabled,
    whereas the cyclic GC is optional and can be used manually.

    In order to decide when to run, each generation has an individual counter and threshold.
    The counter stores the number of object allocations minus deallocations since the last collection.
    Every time you allocate a new container object, CPython checks whenever the counter of the first generation
    exceeds the threshold value.
    If so Python initiates the сollection process.

    """
    import gc

    # We are using ctypes to access our unreachable objects by memory address.
    class PyObject(ctypes.Structure):
        _fields_ = [("refcnt", ctypes.c_long)]
        # pass

    gc.disable()  # Disable generational gc

    lst = []
    lst.append(lst)

    # Store address of the list
    lst_address = id(lst)
    print('lst refcount: {}'.format(sys.getrefcount(lst)))

    # Destroy the lst reference
    del lst

    # print('lst refcount after del: {}'.format(sys.getrefcount(lst)))

    object_1 = {}
    object_2 = {}
    object_1['obj2'] = object_2
    object_2['obj1'] = object_1

    obj_address = id(object_1)
    print('obj_add')

    print('obj1 refcount: {}'.format(sys.getrefcount(object_1)))
    print('obj2 refcount: {}'.format(sys.getrefcount(object_2)))
    # Destroy references
    del object_1, object_2

    # print('obj1 refcount: {}'.format(sys.getrefcount(object_1)))
    # print('obj2 refcount: {}'.format(sys.getrefcount(object_2)))

    # Uncomment if you want to manually run garbage collection process
    # gc.collect()

    # Check the reference count
    print(PyObject.from_address(obj_address).refcnt)
    print(PyObject.from_address(lst_address).refcnt)


simple_refcount()
# ggc()
