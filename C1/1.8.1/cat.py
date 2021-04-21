class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print_cat(self):
        print(f"Имя: {self.name}")
        print(f"Пол: {self.gender}")
        print(f"Возраст: {self.age}")
