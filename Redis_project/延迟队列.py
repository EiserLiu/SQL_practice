import time
import uuid
import threading

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def delayTask(name, delayTime):
    task_id = str(uuid.uuid4())

    processTime = time.time() + delayTime
    r.zadd("delay-queue", {name + task_id: processTime})


def loop():
    while True:
        task_list = r.zrangebyscore("delay-queue", 0, time.time(), 0, 1)
        if not task_list:
            print("cost 1秒")
            time.sleep(1)
            continue

        task_id = task_list[0]
        ok = r.zrem("delay-queue", task_id)
        if ok:
            handleTask(task_id)


def handleTask(task_id):
    print(f"任务{task_id}执行完毕!")


t = threading.Thread(target=loop)
t.start()

delayTask("任务1", 5)
delayTask("任务2", 2)
delayTask("任务3", 4)
delayTask("任务4", 10)
delayTask("任务5", 15)
