from datetime import datetime
from flask import Flask, flash, request, render_template
from tinydb import TinyDB


app = Flask(__name__)
app.secret_key = 'secret-key'
db = TinyDB('db.json')


@app.route('/', methods=['POST', 'GET'])
def start_page():
    flash('Вас приветствует обработчик POST запросов!')
    flash('На вход передаются данные такого вида: `f_name1=value1&f_name2=value2`')

    return render_template('index.html')


@app.route('/get_form', methods=['POST', 'GET'])
def get_form():
    input_user = str(request.form["name_input"])
    result_list = handler_btn(input_user)
    flash(f'Было: {input_user}')
    flash(f'Стало: {result_list}')
    flash(f'База данных целиком: {db.all()}')

    # добавляем ответ пользователя в БД
    [db.update({i: result_list.get(i)}, doc_ids=[1]) for i in result_list]

    # тестовые варианты для ввода:
    #   f_name1=11.11.2011&f_name2=2011-11-11&f_name3=+7 999 999 99 99&f_name4=test@test.ru&f_name5=test@test.com
    #   f_name6=abrakadabra1&f_name7=abrakadabra@1&f_name8=2011-11-1s

    return render_template('index.html')


def handler_btn(input_user):
    request_split = input_user.split('&')
    request_dict = {i.split('=')[0]: i.split('=')[1] for i in request_split}

    result_dict = {}
    for key in request_dict:
        value = ''.join(request_dict.get(key).split(" "))
        if len(value) == 10:
            try:
                if value.count('.') == 2 and bool(datetime.strptime(value, '%d.%m.%Y')):
                    result_dict[key] = 'date'
                elif value.count('-') == 2 and bool(datetime.strptime(value, '%Y-%m-%d')):
                    result_dict[key] = 'date'
            except:
                result_dict[key] = 'text'
        elif False not in [el.isdigit() for el in value][1:] and value[0] == '+' and len(value) == 12:
            result_dict[key] = 'phone'
        elif value.count('@') == 1:
            if (value[-3:] == '.ru' and value.count('.ru') == 1) or (value[-4:] == '.com' and value.count('.com') == 1):
                result_dict[key] = 'email'
            else:
                result_dict[key] = 'text'
        else:
            result_dict[key] = 'text'
    return result_dict


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
