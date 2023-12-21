import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379, charset="utf-8", decode_responses=True)
# # 1.字符串操作
# r.set('bar','Foo')
# print(r.get('bar'))
#
# # 不允许对已经存在的值进行操作
# ret = r.setnx("name","yuan")
# print(ret)
#
# # 设置键有效期
# r.setex("good1001", 10,"2")
#
# # 自增自减
# r.set("age", 22)
# r.incr("age", 10)
# print(r.get("age"))

# 2.哈希操作
# r.hset("info","name","rain")
# print(r.hget("info","name"))

# r.hset("info", "gender", "male")
# r.hmset("info", {"gender": "male","age": 22})
# print(r.hgetall("info"))

# 3. list操作
r.delete("users")
r.lpush('users', '刘泽普', '赵天宇', '哈字节', '张红菊', '李一凡')
print(r.lrange('users', 0, -1))
print(r.lindex('users', 0))
