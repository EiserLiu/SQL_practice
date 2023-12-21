import redis

# 方式1
# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set("foo", "Bar")

# 方式2
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

r.set('bar', 'Foo')
print(r.get('bar'))
