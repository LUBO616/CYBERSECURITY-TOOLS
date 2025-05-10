import  string
import random

longi= int(input ("Enter the password length: "))

characters= string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(longi))
print(f'The new password is: {password}')