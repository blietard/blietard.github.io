import time
from multiprocessing import Process, Lock, Barrier, cpu_count

def f(l, b, i):
    time.sleep((proc_count-i)/2)
    print("Proc",i,"waiting at barrier.")
    b.wait()
    print("Barrier passed by",i)
    
    # n = 2000
    # _ = [ [ i*j for j in range(n)] for i in range(n) ]
    time.sleep(5)

    l.acquire()
    try:
        print('Locked by', i)
        with open("test.txt","r") as t:
            text = t.read()
        with open("test.txt","w") as t:
            t.write(text+f"Proc {i} was here\n")
        time.sleep(2)
    finally:
        print("Release lock by",i)
        l.release()

if __name__ == '__main__':
    proc_count = mp.cpu_count()
    print("Available CPUs:", proc_count)

    with open("test.txt","w") as t:
        t.write("\n")
    lock = Lock()
    barrier = mp.Barrier(proc_count)
    procs = [ Process(target=f, args=(lock, barrier, num)) for num in range(proc_count) ]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
