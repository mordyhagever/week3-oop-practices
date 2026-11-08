
class User:
    def __init__(self, age):
        self.age = age

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, new_age):
        if new_age < 0 or new_age > 120:
            raise ValueError("age isn't real")
        self.__age = new_age


