from working_with_databases_in_python import  database


MENU_PROMPT = """------ COFFEE BEAN APP--------

Please choose one of these options

1) Add a new bean.
2) See all bean.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.
6) Delete all beans

Your selection:"""


#user code

def menu():
    """
    displays menu and let user interact with menu
    Returns:

    """
    connection = database.connect()
    database.create_table(connection)
    user_input = input(MENU_PROMPT)
    while True :
        print(user_input)
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_display_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean_by_name(connection)
        elif user_input == "4":
            pass
        elif(user_input == "5"):
            print("Thanks for using our app, please visit again.")
            break
        elif(user_input == "6"):
            promp_delete_all_bean_records(connection)
        else:
            print("Invalid option selected, please try again!!")

        user_input = input(MENU_PROMPT)

menu()


def prompt_add_new_bean(connection):
    # add a new bean
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (1-100): "))

    database.add_bean(connection, name, method, rating)


def prompt_display_all_beans(connection):
    # See all bean
    all_records = database.get_all_beans(connection)
    if all_records:
        print("All beans are ---------> ")
        for record in all_records:
            print(record)
    else:
        print("No beans present in our record.")

def prompt_find_bean_by_name(connection):
        # find a bean by name
        name = input("Enter bean name which you want to search: ")
        records = database.get_beans_by_name(connection, name)
        if records is not None:
            for row in records:
                print(row)
        else:
            print("No record here.")

def prompt_best_method_for_preparation(connection):
    # See which prepartion method is best
    name = input("enter the name of the bean for which you want to test preparation: ")
    best = database.get_best_preparation_for_bean(connection, name)
    if best:
        print(best)
    else:
        print("no record present for this name.")

def promp_delete_all_bean_records(connection):
    database.delete_all_beans(connection)
    print("All records deleted........")
