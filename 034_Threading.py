import threading



def Foo(coll: list[int], res_lst) -> int:
    # print(f"{id(res) = } in {threading.current_thread().name}")
    print(f"{coll = } in {threading.current_thread().name}")
    res_lst.append(sum(coll))
    # print(f"{id(res) = } in {threading.current_thread().name}")


def Main(data: list[int]) -> None:
    batch_size = 25
    # res1 = 0
    # res2 = 1
    # res3 = 2
    # res4 = 3

    # print(f"{id(res1) = }")
    # print(f"{id(res2) = }")
    # print(f"{id(res3) = }")
    # print(f"{id(res4) = }")

    lst_res = []

    t1 = threading.Thread(target=Foo, name="Thread_1", args=(lst[0:25], lst_res))
    t2 = threading.Thread(target=Foo, name="Thread_2", args=(lst[25:50], lst_res))
    t3 = threading.Thread(target=Foo, name="Thread_3", args=(lst[50:75], lst_res))
    t4 = threading.Thread(target=Foo, name="Thread_4", args=(lst[75:100], lst_res))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # print(f"{id(res1) = }")
    # print(f"{id(res2) = }")
    # print(f"{id(res3) = }")
    # print(f"{id(res4) = }")


    # print(f"{res1}, {res2}, {res3}, {res4}")
    # final = res1 + res2 + res3 + res4

    print(f"{lst_res = }")
    final = sum(lst_res)
    print(f"Result --> {final}")
    print(final == sum(data))

if __name__ == "__main__":
    lst = [x for x in range(100)]
    Main(lst)

## Thread synchronisation objects
#       * threading.Lock()
#       * threading.RLock()
#       * threading.Semaphore()
#       * threading.BoundedSemaphore()
#       * threading.Condition()
#       * threading.Event()
#       * import queue.Queue()

