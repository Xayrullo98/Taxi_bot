import sqlite3


class Database:
    def __init__(self, baza_manzili):
        self.path_to_db = baza_manzili

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item}=?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM usres:", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

    def user_qoshish(self, ism: str, tg_id: int, username: str = None, ):

        sql = """
           INSERT INTO myfiles_subscribe(ism,  username, tg_id) VALUES(?, ?, ?)
           """
        self.execute(sql, parameters=(ism, username, tg_id), commit=True)

    def select_maxsulot(self, **kwargs):
        sql = "SELECT * FROM maxsulot WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all_maxsulotlar(self):
        sql = """
            SELECT * FROM myfiles_maxsulot
            """
        return self.execute(sql, fetchall=True)

    # course section
    def add_course(self, name: str, text: str, price: int, link: str, channel_id: str):

        sql = """
        INSERT INTO course(name,text,price,link,channel_id) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(name, text, price, link, channel_id), commit=True)

    def select_all_course(self):
        sql = """
            SELECT * FROM course
            """
        return self.execute(sql, fetchall=True)

    def delete_course(self, **kwargs):
        sql = "DELETE  FROM course WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, commit=True)

    def select_course(self, **kwargs):
        sql = "SELECT * FROM course WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    # users section
    def add_user(self, fullname: str, tg_id: str):

        sql = """
        INSERT INTO users(fullname,tg_id) VALUES(?, ?)
        """
        self.execute(sql, parameters=(fullname, tg_id), commit=True)

    def select_all_user(self):
        sql = """
            SELECT * FROM users
            """
        return self.execute(sql, fetchall=True)

    def delete_user(self, **kwargs):
        sql = "DELETE * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, commit=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def update_deadline(self, deadline, id):
        # SQL_EXAMPLE = "UPDATE myfiles_menu SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
           UPDATE course_students SET deadline=? WHERE id=?
           """
        return self.execute(sql, parameters=(deadline, id), commit=True)


def logger(statement):
    print(f"""
    -------------------------------------------------------
    Executing:
    {statement}
    -------------------------------------------------------
""")
