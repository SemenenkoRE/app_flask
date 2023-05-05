
class MssqlConnect:

    __connection = None
    __cursor = None

    def __do_connection(self):

        """ """

        name_user = 'sa'
        name_server = 'localhost'
        password = 'ert!@#ERT'
        name_db = 'db_sales'

        import pymssql

        self.__connection = pymssql.connect(name_server, name_user, password, name_db)
        self.__cursor = self.__connection.cursor()

    def do_select(self, sql_command):

        """ """

        self.__do_connection()

        self.__cursor.execute(sql_command)

        for row in self.__cursor:
            print(row)

        self.__close_connect()

    def do_insert(self, sql_command):

        """ """

        self.__cursor.execute(sql_command)
        self.__do_commit()
        self.__close_connect()

    # @staticmethod
    # def form_command():
    #
    #     return f"INSERT INTO dbo.Inventory VALUES (1, "banana", 150);"

    def __do_commit(self):

        """ """

        self.__connection.commit()

    def __close_connect(self):

        """ """

        self.__connection.close()


if __name__ == "__main__":

    x = MssqlConnect()
    x.do_select('select * from sales;')

