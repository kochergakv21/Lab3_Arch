
import redis


def create(key, data):
    base = redis.StrictRedis(host='localhost', port=6379, db=0)
    if base.set(key, data):
            return 'Document has been added.'
    return 'Document has not been added.'


def read(key):
    base = redis.StrictRedis(host='localhost', port=6379, db=0)
    result = base.get(key)
    if result is None:
        return 'Document has not been read.'
    if len(result) > 0:
        return result


def update(key, data):
    base = redis.StrictRedis(host='localhost', port=6379, db=0)
    result = base.get(key)
    if result is None:
        return "Document doesn't exist."
    base.set(key, data)
    return 'Document has been updated.'


def delete(key):
    base = redis.StrictRedis(host='localhost', port=6379, db=0)
    result = base.get(key)
    if result is None:
        return "Document doesn't exist."
    base.delete(key)
    return 'Document has been deleted.'
