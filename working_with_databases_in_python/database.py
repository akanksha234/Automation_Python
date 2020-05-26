import sqlite3

#contains variables which create a coffee beans table with different methods and name and rating
#database code

CREATE_TABLE_BEANS = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"
GET_ALL_BEANS = "SELECT * FROM beans"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1
"""
DELETE_ALL_BEANS = "DELETE FROM beans"

def connect():
    """
    connects to the sqlite3 database
    Returns:connection object

    """
    connection = sqlite3.connect("data.db")
    return connection

def create_table(connection):
    """
    creates a table beans if it doesn't exist
    Args:
        connection: connection object

    Returns: None

    """
    with connection:
        connection.execute(CREATE_TABLE_BEANS)

def add_bean(connection, name, method, rating):
    """
    Inserts a row with name method and rating of a bean
    Args:
        connection: connection object
        name: name of the bean
        method: method for preparation of bean
        rating: rating of quality of coffe bean

    Returns: NONE

    """
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

def get_all_beans(connection):
    """
    Returns all rows of table bean
    Args:
        connection: connection object

    Returns: all rows of bean table

    """
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_beans_by_name(connection, name):
    """
    Returns all rows of beans with name in parameter
    Args:
        connection: connection object
        name: name of the bean

    Returns: All rows with name as passed in the parameter

    """
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name, )).fetchall()

def get_best_preparation_for_bean(connection, name):
    """
    Returns the row with highest rating in the bean table
    Args:
        connection: connection object
        name: name of the bean

    Returns:

    """
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, name).fetchone()

def delete_all_beans(connection):
        """
        Deletes all records of the bean from the table
        Args:
            connection: connection object

        Returns:None
        """
        connection.execute(DELETE_ALL_BEANS)


