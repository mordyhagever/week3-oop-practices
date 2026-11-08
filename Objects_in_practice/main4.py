from classes.tar4 import User

user = User(30)
user.get_age = user.age + 1
print(user.get_age)
try:
    user.get_age = -5
except ValueError as error:
    print("error", error)
print(user.get_age)