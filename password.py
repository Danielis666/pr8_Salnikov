import random

pull = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
output = ''
for i in range(11):
    output += random.choice(pull)
print(output)
