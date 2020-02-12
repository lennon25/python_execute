import hashlib, random
import hmac

db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))

	if user in db.keys():
		return db[user] == md5.hexdigest()
	else:
		return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')



# 加盐的hash算法
def get_md5(s):
	return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
	def __init__(self,username, password):
		self.username = username
		self.salt = ''.join([chr(random.randint(48,122))for i in range(20)])
		self.password = get_md5(password + self.salt)


def login(username, password):
	user = db[username]
	return User.password == get_md5(password + User.slat)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# hmac算法
message = b'Hello, World!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
h.hexdigest()


