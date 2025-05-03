class PhoneBook():
    def __init__(self):
        self.hashmap = dict()

    def add_contact(self, name: str, number: str):
        if name not in self.hashmap:
            self.hashmap[name] = number
        else:
            raise KeyError(f"Contact '{name}' already exists")


    def get_number(self, name: str):
        try:
            return self.hashmap[name]
        except KeyError:
            raise KeyError(f"Contact '{name}' not found")

    def update_contact(self, name: str, new_number: str):
        if name not in self.hashmap:
            raise KeyError(f"Contact '{name}' not found")
        self.hashmap[name] = new_number

    def remove_contact(self, name: str):
        try:
            del self.hashmap[name]
        except KeyError:
            raise KeyError(f"Contact '{name}' not found")

    def has_contact(self, name: str):
        if name in self.hashmap:
            return True
        return False

    def all_contacts(self):
        return list(self.hashmap.keys())