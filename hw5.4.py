from functools import wraps


def input_error(func): # wraps decorator to handle exceptions and return user-friendly messages
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input): # splits the user input into command and arguments
    parts = user_input.split()
    if not parts:
        return "",
    cmd, *args = parts
    return cmd.lower(), *args


@input_error
def add_contact(args, contacts):    # adds a new contact to the contacts dictionary
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):     # changes the phone number of an existing contact in the contacts dictionary
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):     # shows the phone number of a contact in the contacts dictionary
    name = args[0]
    return f"{name}: {contacts[name]}"


def show_all(contacts):     # shows all contacts in the contacts dictionary
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():     #   main function to run the assistant bot
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGood bye!")
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
