import sqlite3


class DatabaseManager():
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor


    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def commit(self):
        self.connection.commit()

    def create_table(self):
        self.execute("CREATE TABLE IF NOT EXISTS passes(site TEXT, username TEXT, password TEXT)")

    def execute_query(self, query, args=None):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error executing SQL query:", e)
            return None

    def get_password(self, site, username):
        query = 'SELECT password FROM passes WHERE site=? AND username=?'
        result = self.execute_query(query, (memoryview(site), memoryview(username)))
        if result:
            return result[0][0]
        else:
            return None

    def insert_password(self, site, username, password):
        query = 'INSERT INTO passes(site, username, password) VALUES(?,?,?)'
        self.execute_query(query, (site, username, password))
        self.commit()

    def delete_account(self, site, username):
        result = self.get_password(site, username)

        if result:
            print("Deleted {} acc at {}".format(username, site))
            self.execute_query('DELETE FROM passes WHERE site=? AND username=?', (site, username))
            self.commit()
            return True
        else:
            print("Not found {} -> {}".format(site, username))
            return False