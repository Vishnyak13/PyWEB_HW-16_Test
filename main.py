from sqlalchemy.exc import SQLAlchemyError

from database.seed import (
    create_fake_contacts,
    add_contact,
    get_contact_by_id,
    get_all_contacts,
    update_contact,
    delete_contact,
    add_phone,
    add_email,
    add_address,
)
from styles.styles import *


def match_case(choice):
    try:
        match choice:
            case 1:
                print(get_all_contacts())
            case 2:
                print(get_contact_by_id(int(input("Enter id: "))))
            case 3:
                print(
                    add_contact(
                        input("Enter first name: "),
                        input("Enter last name: "),
                        input("Enter address: "),
                    )
                )
            case 4:
                print(
                    update_contact(
                        int(input("Enter id: ")),
                        input("Enter first name: "),
                        input("Enter last name: "),
                        input("Enter address: "),
                    )
                )
            case 5:
                print(delete_contact(int(input("Enter id: "))))
            case 6:
                print(
                    add_phone(int(input("Enter id: ")), input("Enter phone number: "))
                )
            case 7:
                print(
                    add_email(int(input("Enter id: ")), input("Enter email address: "))
                )
            case 8:
                print(add_address(int(input("Enter id: ")), input("Enter address: ")))
    except SQLAlchemyError as e:
        error_text(e)


def run():
    try:
        while True:
            title_text("What do you want to do?")
            option_text("1. Get all contacts")
            option_text("2. Get contact by id")
            option_text("3. Add contact")
            option_text("4. Update contact")
            option_text("5. Delete contact")
            option_text("6. Add phone number to contact")
            option_text("7. Add email address to contact")
            option_text("8. Add address to contact")
            option_text("9. Exit")
            choice = int(input("Enter choice: "))
            if choice == 9:
                print("Goodbye")
                break
            match_case(choice)
    except ValueError:
        error_text("Please enter a number")
        run()


def main():
    title_text("Welcome to Address Book")
    print("Do you want to create fake contacts? (y/n)")
    if input(">>>: ") == "y":
        try:
            print("How many contacts do you want to create?")
            create_fake_contacts(int(input("Enter count: ")))
            run()
        except SQLAlchemyError as e:
            error_text(e)
    else:
        print("Ok, no fake contacts")
        run()


if __name__ == "__main__":
    main()
