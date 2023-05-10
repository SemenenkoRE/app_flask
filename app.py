from flask import Flask, render_template, request, send_file, url_for, redirect    # flash, session

# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer


ALLOWED_EXTENSIONS = ('xlsx')

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/query", methods=["POST", "GET"])
def select():

    """ Возвращает страницу для формирования выгрузки из БД """

    if request.method == 'GET':

        return render_template('index.html')

    elif request.method == 'POST':

        # Получить словарь с запросом
        dict_query = request.form.to_dict()

        # Сформировать команду запроса
        from form_query import SelectQuery
        proc = SelectQuery(dict_query)
        sql_command = proc.get_query

        # Выполнить запрос и сохранить файл
        from do_unload import UnloadQuery
        UnloadQuery(sql_command)

        # Выгружаем файл
        path_file = UnloadQuery.set_directory()

        return send_file(path_file + '/files/report1.xlsx', as_attachment=False)

        return redirect(url_for('select'))


@app.route("/pivot", methods=["POST", "GET"])
def pivot():

    """ Возвращает страницу для формирования выгрузки из БД """

    if request.method == 'GET':

        return render_template('pivot.html')

    elif request.method == 'POST':

        # Получить словарь с запросом
        dict_query = request.form.to_dict()

        print('dict_query --- ', dict_query)

        # Сформировать команду запроса
        from form_pivot import SelectQueryPivot
        proc = SelectQueryPivot(dict_query)
        sql_command = proc.get_query

        # Выполнить запрос и сохранить файл
        from do_pivot import UnloadPivot
        UnloadPivot(sql_command)

        # Выгружаем файл
        path_file = UnloadPivot.set_directory()

        return send_file(path_file + '/files/report2.xlsx', as_attachment=False)

        return redirect(url_for('pivot'))


@app.route("/insert", methods=["POST", "GET"])
def insert():

    """ Возвращает страницу для занесения данных в БД """

    if request.method == 'GET':

        return render_template('insert.html')

    elif request.method == 'POST':

        # Получить словарь с запросом
        dict_query = request.form.to_dict()

        # Сформировать команду запроса
        from form_insert import InsertQuery
        proc = InsertQuery(dict_query)
        sql_command = proc.get_query

        # Выполнить запрос и сохранить файл
        from do_insert import InsertQuery
        InsertQuery(sql_command)

        return redirect(url_for('insert'))


if __name__ == "__main__":

    app.run(debug=True)
