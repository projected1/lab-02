import uuid


class Customer:
    def __init__(self, name, city, age):
        self.id = uuid.uuid4()
        self.name = name
        self.city = city
        self.age = age

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return 'Customer id: %s, name: %s, city: %s, age: %s' % \
            (self.id, self.name, self.city, self.age)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
