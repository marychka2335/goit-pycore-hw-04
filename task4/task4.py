from contact_bot import (add_contact, change_contact, get_contact, get_all_contacts)

COMMAND_ALL = {"all"}
COMMAND_ADD = {"add"}
COMMAND_CHANGE = {"change"}
COMMAND_PHONE = {"phone"}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in COMMAND_ADD:
            print(add_contact(args, contacts))
        elif command in COMMAND_CHANGE:  
            print(change_contact(args, contacts))
        elif command in COMMAND_PHONE:
            print(get_contact(args, contacts))
        elif command in COMMAND_ALL:
            print(get_all_contacts(contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()