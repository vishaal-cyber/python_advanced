import threading



def Foo(coll: list[int], res) -> int:
    print(f"{id(res) = } in {threading.current_thread().name}")
    res =  sum(coll)


def Main(data: list[int]) -> None:
    batch_size = 25
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0

    print(f"{id(res1) = }")
    print(f"{id(res2) = }")
    print(f"{id(res3) = }")
    print(f"{id(res4) = }")

    t1 = threading.Thread(target=Foo, name="Thread_1", args=(lst[0:25], res1))
    t2 = threading.Thread(target=Foo, name="Thread_2", args=(lst[25:50], res2))
    t3 = threading.Thread(target=Foo, name="Thread_3", args=(lst[50:75], res3))
    t4 = threading.Thread(target=Foo, name="Thread_4", args=(lst[75:100], res4))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(f"{res1}, {res2}, {res3}, {res4}")
    final = res1 + res2 + res3 + res4
    print(f"Result --> {final}")
    print(final == sum(lst))

if __name__ == "__main__":
    lst = [x for x in range(100)]
    Main(lst)
