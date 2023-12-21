import redis

r = redis.Redis(host='127.0.0.1')

r.publish("room_101", "hello Eiser")