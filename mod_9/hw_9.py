
COMMANDS_NAME = ('add', 'change', 'phone')

contacts = {}

def command_error(func):
    
    def inner(respond):
        
        try:
            command_func, contacts_information = func(respond)
            command_func(contacts_information)
    
        except KeyError:
            print(f'\nI don\'t know such command: "{respond}".\
                  \nEnter, please: add|change|phone \n')
            
        except ValueError:
            print(f'\nGive me CONTACT INFORMATION to fulfill: "{respond}"\n')
            
        except TypeError:
            just_answer = command_func
            print(just_answer)
        
    return inner


def input_error(func):
    
    def inner(contacts_information):
        
        try:
            func(contacts_information)
            
        except KeyError:
            print('\nSuch contact doesn\'t exist\n')

        except NameError:
            print('\nSuch contact has already added. Please, use command "change"')

        except:
            print('\nGive me NAME and PHONE please (must be space between name and phone)')
        
    return inner

@command_error
def handler(respond):
    contacts_information = ''
    if respond.startswith(COMMANDS_NAME):
        respond, contacts_information = respond.split(' ', 1)
    command = commands[respond]
    return command, contacts_information


@input_error
def add_contact(contacts_information):
    global contacts
    name, phone_number = contacts_information.split()
    if contacts.get(name, False):
        raise NameError
    contacts[name] = phone_number
    print(f'\nContacts with "{name.capitalize()} : {phone_number}" - were successfully saved')
@input_error
def change_contact(contacts_information):
    name, phone_number = contacts_information.split()
    if contacts[name]:
        contacts[name] = phone_number
        print(f'\n{phone_number} of {name.capitalize()} was successfully changed')
@input_error
def phone_number(contacts_information):
    result = contacts[contacts_information]
    print(f"\nThe phone of {contacts_information.capitalize()} is {result}")

def show_numbers(contacts_information):#there isn't be argument
    print('\nThere is a list of contacts:')
    for contact, phone in contacts.items():
        print(f'{contact.capitalize()} : {phone}')
              

commands = {
            'hello': '\nHow can I help you?',
            'add': add_contact,
            'change': change_contact,
            'phone': phone_number,
            'show all': show_numbers
            }

def main():
    
    print('Hello. I\'m console bot')
    
    while True:
        
        respond = input('\nYou: ')
        respond = respond.lower()
        
        if respond in ("good bye", "close", "exit"):
            print('\nGood bye!')
            break
        
        handler(respond)

if __name__ == '__main__':
    main()
