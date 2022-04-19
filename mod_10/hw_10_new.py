from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Name(Field):
    pass

        
class Phone(Field):
    def __eq__(self, other):
        return self.value == other.value
    

class Email(Field):
    pass


class AddressBook(UserDict):

    def add_record(self, record):
        self.record = record
        self.data[self.record.name.value] = self.record
        
    def del_record(self):
        self.data.popitem()


class Record:
    
    def __init__(self, name: Name, phone: Phone = None, email: Email = None):
        self.name = name
        self.email = email
        self.phones = []

        if phone:
            self.phones.append(phone)
        
    def add(self, phone):
        self.phones.append(phone)

    def change(self, old_phone, new_phone):
        self.phones.remove(old_phone)
        self.phones.append(new_phone)

    def del_phone(self, phone):
        self.phones.remove(phone)





if __name__ == "__main__":
    name_1 = Name('Bob')
    phone_1 = Phone('0000')
    
    r = Record(name_1, phone_1, "aaa@gmail.com")
    print(r.name, r.phones, r.email)
    
    a = AddressBook()
    print(f"AddressBook - {a}")
    
    a.add_record(r)
    print(f"AddressBook - {a}")
    print(a['Bob'].phones)

    phone_2 = Phone('1111')
    r.add(phone_2)
    print(r.name, r.phones)

    
    phone_3 = Phone('2222')
    r.change(phone_1, phone_3)
    print(a['Bob'].phones)

    a["Bob"].del_phone(phone_3)
    print(a['Bob'].phones)

    r.change(Phone('1111'), Phone('5555'))
    print(a['Bob'].phones)

