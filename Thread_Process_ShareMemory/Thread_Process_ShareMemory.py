import multiprocessing as mp
import threading as td
import time

'''
多进程》正常》多线程    时间上
'''

def job(q):
    print("aaaaaa")
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    # 多进程不能return 值
    # queue：队列，用于多进程、多线程通信
    q.put(res)


def job1(x):
    return x * x

def use_thread():
    # 多线程
    t1 = td.Thread(target=job, args=(1, 2))
    t1.start()
    # 等待线程执行完毕。
    t1.join()
def use_process():
    # 创建一个队列，进程间通信对象
    q = mp.Queue()
    # 多进程
    # 当args只有一个参数时，后+逗号表示可迭代
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1, res2)
def process_pool():
    # 创建进程池，指定进程数为2
    pool = mp.Pool(processes=2)
    # 使用map方法并行执行任务，将结果存储在列表中
    res = pool.map(job1, range(10000))
    print(res)
    # 使用apply_async方法异步执行任务，并通过get方法获取结果
    res = pool.apply_async(job1, (2,))
    print(res.get())
    # 使用列表推导式和apply_async方法并行执行多个任务
    multi_res = [pool.apply_async(job1, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])
def share_memory_show():
    # value：共享的值
    value = mp.Value('d', 1)
    # 必须一维的（列表）
    array = mp.Array('i', [1, 2, 3])
def job2(v, num, l):
    # 锁住
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    # 锁释放
    l.release()
# 共享值、列表等
def share_memory():
    l = mp.Lock()
    # value：共享的值
    value = mp.Value('d', 1)
    # 共享的，必须一维的（列表）
    array = mp.Array('i', [1, 2, 3])
    p1 = mp.Process(target=job2, args=(value, 1, l))
    # p2进程会被锁阻塞
    p2 = mp.Process(target=job2, args=(value, 2, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''
进程通信：     pipe 双向通信      queue 单向通信
进程共享：     Value，Array，List，Dict
进程同步：     Rlock
'''
if __name__ == '__main__':
    share_memory()
