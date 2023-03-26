import random

pull = '1234567890'
output = ''
for i in range(11):
    output += random.choice(pull)
print(output)
