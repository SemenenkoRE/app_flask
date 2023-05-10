
class SelectQuery:

    """
    Объект формирует текст запроса Select для выгрузки записей продаж

    Запрос сформируется даже, если в приложение потребуется прибавить полей для ввода данных
    или к таблице SQL прибавится новые поля.

    """

    __query_text = 'SELECT * FROM sales WHERE'

    __column_sql = {'date_from': 'dat',
                    'date_until': 'dat',
                    'articul': 'article',
                    'weight_until': 'weight',
                    'weight_from': 'weight'
                    }

    def __init__(self, dict_order):

        """ Инициализатор класса.
        dict_order - словарь с данными, полученными от приложения
        """

        pars_order = self.__del_empty(dict_order)
        self.__do_query(pars_order)

    def __del_empty(self, dict_order):

        """ Сфомировать словорь без пустых значений """

        pars_order = {}

        for key, val in dict_order.items():
            if val != '':
                pars_order[key] = val

        return pars_order

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

        self.__query_text = f"{self.__query_text};"

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

    x = SelectQuery({'date_from': '', 'date_until': '', 'articul': '10000004', 'weight_until': '1', 'weight_from': '20'})
    print(x.get_query)
