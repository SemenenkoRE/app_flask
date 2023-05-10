
class SelectQueryPivot:

    """
    Объект формирует текст запроса (Select) для получения сводного отчета

    Запрос сформируется даже, если в приложение потребуется прибавить полей для ввода данных
    или к таблице SQL прибавится новые поля.

    """

    __column_sql = {'date_from': 'dat',
                    'date_until': 'dat',
                    'articul': 'article',
                    }

    def __init__(self, dict_order):

        """ Инициализатор класса.
        dict_order - словарь с данными, полученными от приложения
        """

        self.__query_text = f"SELECT YEAR(dat), MONTH(dat), article, SUM(weight), (SELECT SUM(weight) FROM sales WHERE article = {dict_order['articul']}), ROUND(SUM(weight) / (SELECT SUM(weight) FROM sales WHERE article = {dict_order['articul']}), 4) FROM sales WHERE"

        self.__do_query(dict_order)

    def __do_query(self, dict_order):

        """ Сформировать команду SQL """

        # Параметр (как флаг) отвечает за то, есть ли хотя бы одно сравнение внутри
        first_filter = False

        for key, val in dict_order.items():
            if 'until' in key:
                self.__query_text = self.__form_text(key,
                                                     val,
                                                     first_filter,
                                                     '<=')
            elif 'from' in key:
                self.__query_text = self.__form_text(key,
                                                     val,
                                                     first_filter,
                                                     '>=')
            else:
                self.__query_text = self.__form_text(key,
                                                     val,
                                                     first_filter,
                                                     '=')

            first_filter = True

        self.__query_text = f"{self.__query_text} GROUP BY YEAR(dat), MONTH(dat), article;"

    def __form_text(self, key, val, first_filter, oper):

        """ """
        if 'date' not in key:
            return f"{self.__query_text}{' And ' if first_filter else ' '}{self.__column_sql[key]} {oper} {val}"
        else:
            return f"{self.__query_text}{' And ' if first_filter else ' '}{self.__column_sql[key]} {oper} '{val}'"

    @property
    def get_query(self):

        """ Вернуть команду """

        return self.__query_text


if __name__ == '__main__':

    x = SelectQueryPivot({'date_from': '', 'date_until': '', 'articul': '10000004'})
    print(x.get_query)
