import random
import string

n = 12

letras = string.ascii_letters + string.digits + string.punctuation
result_psw = ''.join(random.choice(letras) for i in range(n))

def get_new_psw():
	result_psw = ''.join(random.choice(letras) for i in range(n))
	return result_psw

print(result_psw)
