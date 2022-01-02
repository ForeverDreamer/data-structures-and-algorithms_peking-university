import hashlib


def utf8_encode(s):
    # print(s.encode('utf-8'))
    return s.encode('utf-8')


print(hashlib.md5(utf8_encode('hello world!')).hexdigest())
print(hashlib.sha1(utf8_encode('hello world!')).hexdigest())

m = hashlib.md5()
m.update(utf8_encode('hello world!'))
m.update(utf8_encode('this is part #2'))
m.update(utf8_encode('this is part #3'))
print(m.hexdigest())
