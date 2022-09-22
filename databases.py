import sqlite3

conn = sqlite3.connect("pass_man.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS passman_table (
            id INTEGER PRIMARY KEY,
            email TEXT,
            website TEXT,
            password TEXT
            )""")


def insert_info(obj):
    with conn:
        cursor.execute(f"INSERT INTO passman_table (email, website, password) "
                       f"VALUES ('{obj.email}', '{obj.website}', '{obj.password}')")


# new = Passman('testuser', 'testemail@gmail.com', 'www.testwebsite.org', 'tespassword')


def get_info(info):
    cursor.execute("SELECT * FROM passman_table WHERE website LIKE :info_search", {'info_search': f'{info}%'})
    return cursor.fetchall()


def update_info(obj, password):
    with conn:
        cursor.execute("""UPDATE passman_table SET pay = :pay
                    WHERE first = :first AND last = :last""",
                       {'user': obj.username, 'email': obj.email, 'password': password})


#
#
def remove_info(obj):
    with conn:
        cursor.execute("DELETE from passman_table WHERE user = :user AND email = :email",
                       {'user': obj.username, 'email': obj.email})

# remove_emp(new)