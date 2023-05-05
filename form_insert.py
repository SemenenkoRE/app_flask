
class InsertQuery:

    """ Объект формирует текст команды Insert """

    __query_text = ''

    __column_sql = ('dat', 'article', 'weight')

    def __init__(self, dict_order):

        """ Инициализатор класса.
        dict_order - словарь с данными, полученными от приложения """

        self.__do_query(dict_order)

    def __do_query(self, dict_order):

        """ Сформировать команду SQL """

        array_val = []

        for val in dict_order.values():
            array_val.append(val)

        self.__query_text = f"INSERT INTO sales (dat, article, weight) VALUES ('{array_val[0]}', {int(array_val[1])}, {int(array_val[2])});"

    @property
    def get_query(self):

        """ Вернуть команду """

        return self.__query_text


if __name__ == '__main__':

    i = InsertQuery({'date': '', 'articul': '10000004', 'weight': '1'})
    print(i.get_query)