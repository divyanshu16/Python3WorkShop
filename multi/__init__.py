"""

multithreading to use when I/O bound operation happens
multiprocessing when CPU bound
"""


"""
As to Pool.close(), 
you should call that when - and only when - you're never going to submit more work to the Pool instance. 
So Pool.close() is typically called when the parallelizable part of your main program is finished. 
Then the worker processes will terminate when all work already assigned has completed.



It's also excellent practice to call Pool.join() to wait for the worker processes to terminate. 
Among other reasons, there's often no good way to report exceptions in parallelized code (exceptions occur in a context 
only vaguely related to what your main program is doing), and 
Pool.join() provides a synchronization point that can report some exceptions that occurred in worker processes that
 you'd otherwise never see.
"""