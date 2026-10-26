from repository.users_repository import get_all_users,get_user_by_id,create_user,update_user,delete_user
from db.db import get_connection

if __name__ == "__main__":
    continue_app = True

    with get_connection() as conn:
        while continue_app:
            print("menu")
            print("1 list users")
            print("2 user by id")
            print("3 create user")
            print("4 update user")
            print("5 delete user")
            print("6 Quit")
            choice = input("Enter your choice")

            match choice:
                case "1":
                    for v in get_all_users(conn):
                        print(v)
                case "2":
                    id = input("Enter the user id")
                    user = get_user_by_id(conn,id)
                    print(user)
                case "3":
                    email = input("Enter the email")
                    lastname = input("Enter the last_name")
                    role = input("Enter the role")
                    id = create_user(conn,email,lastname,role)
                    print(f"The user was successfully created with id {id}")
                case "4":
                    id = input("Enter the user id")
                    email = input("Enter the email")
                    lastname = input("Enter the last_name")
                    count = update_user(conn,email,lastname,id)
                    print(f"{count} rows were updated")
                case "5":
                    id = input("Enter the id of the user to delete")
                    count = delete_user(conn,id)
                    print(f"{count} rows were deleted")
                case "6":
                    print("Thanks, see you soon")
                    continue_app = False

