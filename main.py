# Домашка к уроку 10.2
# Основной модуль запуска декораторов
from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

data = get_all()
app = Flask(__name__)


@app.route("/")
def page_index():
    """
    Деоратор без параметров -вывод всего списка кандидатов
    """
    str_ = '<pre>'
    for i in data:
        str_ += f"{i} \n \n"
    return str_ + '</pre>'


@app.route('/candidates/<int:pk>')
def get_user(pk):
    """
    Вывод одно кандидата по номеру
    """
    user = get_by_pk(pk, data)
    if user:
        str_ = f'<img src="{user.picture}">'
        str_ += f'<pre>{user}</pre>'
    else:
        str_ = 'NOT FOUND'
    return str_


@app.route("/skills/<skill>")
def get_skill(skill):
    """
    Вывод списка кандидатов с введенным навыком
    """
    user = get_by_skill(skill.lower(), data)
    str_ = '<pre>'
    if user:
        for i in user:
            str_ += f"{i} \n \n"
    else:
        str_ = 'NOT FOUND'
    return str_ + '</pre>'


if __name__ == '__main__':
    app.run(port=5000)
