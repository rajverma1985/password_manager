from models import Passman
import sqlite3

conn = sqlite3.connect("pass_man.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS passman_table (
            id INTEGER PRIMARY KEY,
            user TEXT,
            email TEXT,
            website TEXT,
            password TEXT
            )""")


def insert(obj):
    with conn:
        cursor.execute(f"INSERT INTO passman_table (user, email, website) "
                       f"VALUES ('{obj.username}', '{obj.email}', '{obj.website}')")


new = Passman('testuser', 'testemail@gmail.com', 'www.testwebsite.org', 'tespassword')


def get_info(username):
    cursor.execute("SELECT * FROM passman_table WHERE username=:user", {'user': username})
    return cursor.fetchall()


def update_pay(obj, password):
    with conn:
        cursor.execute("""UPDATE passman_table SET pay = :pay
                    WHERE first = :first AND last = :last""",
                       {'user': obj.username, 'email': obj.email, 'password': password})


#
#
def remove_emp(obj):
    with conn:
        cursor.execute("DELETE from passman_table WHERE user = :user AND email = :email",
                       {'user': obj.username, 'email': obj.email})


insert(new)
# remove_emp(new)
