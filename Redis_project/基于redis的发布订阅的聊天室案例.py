import redis
import threading

r = redis.Redis(host='127.0.0.1')


def recv_msg():
    pub = r.pubsub()

    pub.subscribe("room_101")
    pub.parse_response()

    while 1:
        res_msg = pub.parse_response()
        print(">>>", res_msg)


def sand_msg():
    msg = input(">>>")
    r.publish("room_1001", msg)


t = threading.Thread(target=sand_msg)
t.start()

recv_msg()
