import random
import string

n = 12

letras = string.ascii_letters + string.digits + string.punctuation
result_psw = ''.join(random.choice(letras) for i in range(n))

print(result_psw)
