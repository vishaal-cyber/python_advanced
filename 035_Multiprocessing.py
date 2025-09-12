## THREADING #####################################

# import threading

# def do_some_work(val):
#     print("Doing some work in the thread")
#     print(f"echo: {val}")
#     return

# val  = "text"
# t = threading.Thread(target=do_some_work, args=(val,))            # Args in threading can be picklable or non-picklable
# t.start()
# t.join()

# print("Done with threads")




## MULTITHREADING #################################

import multiprocessing

def do_some_work(val):
    print("Doing some work in the thread")
    print(f"echo: {val}")
    return

def Main():
    val  = "text"
    # val = [1, 2, 3, 4, 5]
    # val.append(lambda x: x**2)
    t = multiprocessing.Process(target=do_some_work, args=(val,))       # Args in multiprocessing HAS to be picklable only
    t.start()
    t.join()

    print("Done with processes")

if __name__ == "__main__":
    Main()


## Picklable Objects: 
#   * None, True, False
#   * Integers, Floats, Complex
#   * Normal and Unicode strings
#   * Collections containing only picklable objects
#   * Top level functions
#   * Classes with picklable attributes.
# 
# Non-Picklable objects
#   * Open file handles
#   * Thread objects
#   * Lock/Semaphores
#   * Generators
#   * Open sockets
#   * Db Connections
#   * Inner Functions
#   * Lambdas
#  




## Look up more...
#   Synchronisation of Threads and Processes
#   Pools nad methods (apply, map, and the async versions of these)
#   concurrent.Future
#   couroutines
#   Event loops
#   Gather
#   Asyncio libraries (aiohttp, aiofiles) 
#   https://github.com/python/asyncio
#   https://github.com/aio-libs