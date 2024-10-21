
#Executing SQL commands in Python

import sqlite3

def execute_sql_command(command, params=None):
    # Connect to the database
    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Execute the SQL command
        if params:
            cursor.execute(command, params)
        else:
            cursor.execute(command)

        # Fetch results if it's a SELECT query
        if command.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            return results
        else:
            # Commit the changes for other types of queries
            conn.commit()
            return f"Command executed successfully. Rows affected: {cursor.rowcount}"

    except sqlite3.Error as e:
        return f"An error occurred: {e}"

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Example usage
create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""

insert_user = "INSERT INTO users (name, email) VALUES (?, ?)"
select_users = "SELECT * FROM users"

print(execute_sql_command(create_table))
print(execute_sql_command(insert_user, ('John Doe', 'john@example.com')))
print(execute_sql_command(select_users))