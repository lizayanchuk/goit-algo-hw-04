# Завдання 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_number(args, contacts):
    if len(args) < 2:
        return "Please provide both name and new number."
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact changed."
    return "Contact not found"

def show_phone(args, contacts):
    if not args:
        return "Please provide a name."
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found"

def show_all_numbers(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts found"

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
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_number(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "showall":
            print(show_all_numbers(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
