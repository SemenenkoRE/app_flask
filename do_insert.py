
class InsertQuery:

    __connection = None
    __cursor = None
    __log = ''
    __directory = ''

    def __init__(self, content_command):

        self.__do_connection()
        self.__insert_row(content_command)
        self.__do_commit()
        self.__close_connect()

    def __do_connection(self):

        """ """

        name_user = 'sa'
        name_server = 'localhost'
        password = 'ert!@#ERT'
        name_db = 'db_sales'

        import pymssql

        self.__connection = pymssql.connect(name_server, name_user, password, name_db)
        self.__cursor = self.__connection.cursor()

    def __insert_row(self, content_command):

        """ """
        self.__cursor.execute(content_command)
        self.__do_commit()

    def __do_commit(self):

        """ """

        self.__connection.commit()

    def __close_connect(self):

        """ """

        self.__connection.close()


if __name__ == '__main__':

    pass
