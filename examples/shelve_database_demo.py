import sys, shelve


def store_person(db):
    """
    让用户输入数据，并将其存储到shelve对象中
    """
    pid = input("Enter unique ID number: ")
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):
    """
    让用户输入ID和所需的字段，并从shelve对象中获取相应的数据
    """
    pid = input("Enter unique ID number: ")
    field = input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()

    print(field.capitalize() + ':', db[pid][field])

def print_help():
    pass
