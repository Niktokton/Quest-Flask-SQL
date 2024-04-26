from flask import Flask, url_for, render_template, request, jsonify
import datetime
from data import db_session
from data.results import result


class Timer:
    def __init__(self, current_time):
        self.current_time = current_time

    def decrement(self):
        if self.current_time > -1:
            self.current_time = self.current_time + 1
        return self.current_time


db_session.global_init("db/results.db")
app = Flask(__name__)
t = Timer(current_time=0)
username = 'Имя Игрока'
time = ''


@app.route('/', methods=['GET', 'POST'])
def main():
    global username
    if request.method == 'POST':
        username = request.form['username']
        return render_template('main.html',
                               title='Квест "Скрытые секреты"',
                               username=username,
                               hide='unhidden')
    else:
        return render_template('main.html',
                               title='Квест "Скрытые секреты"',
                               username=username,
                               hide='hidden')


@app.route('/quest1', methods=['GET', 'POST'])
def quest1():
    if request.method == 'POST' and request.form['qst1'] == 'очень простой':
        return render_template('quest_1.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 1: Пароль',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_1.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 1: Пароль',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest2', methods=['GET', 'POST'])
def quest2():
    if request.method == 'POST' and request.form['qst1'] == '1':
        return render_template('quest_2.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 2: Будильник',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_2.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 2: Будильник',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest3', methods=['GET', 'POST'])
def quest3():
    if request.method == 'POST' and request.form['qst1'] == '2':
        return render_template('quest_3.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 3: Математики в баре',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_3.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 3: Математики в баре',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest4', methods=['GET', 'POST'])
def quest4():
    if request.method == 'POST' and request.form['qst1'] == '10':
        return render_template('quest_4.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 4: Рыбок жалко',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_4.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 4: Рыбок жалко',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest5', methods=['GET', 'POST'])
def quest5():
    if request.method == 'POST' and request.form['qst1'] == '1':
        return render_template('quest_5.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 5: Кошки в коробке',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_5.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 5: Кошки в коробке',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest6', methods=['GET', 'POST'])
def quest6():
    if request.method == 'POST' and request.form['qst1'] == '18':
        return render_template('quest_6.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 6: Треугольники',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_6.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 6: Треугольники',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest7', methods=['GET', 'POST'])
def quest7():
    if request.method == 'POST' and request.form['qst1'] == '1':
        return render_template('quest_7.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 7: Асфальт',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_7.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 7: Асфальт',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest8', methods=['GET', 'POST'])
def quest8():
    if request.method == 'POST' and request.form['qst1'] == '87':
        return render_template('quest_8.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 8: Машина на парковке',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_8.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 8: Машина на парковке',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest9', methods=['GET', 'POST'])
def quest9():
    if request.method == 'POST' and request.form['qst1'] == 'случайно':
        return render_template('quest_9.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 9: Производственный брак',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_9.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 9 : Производственный брак',
                               fm='unhidden',
                               hide='hidden')


@app.route('/quest10', methods=['GET', 'POST'])
def quest10():
    if request.method == 'POST':
        return render_template('quest_10.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 10: Жак Фреско',
                               fm='hidden',
                               hide='unhidden')
    else:
        return render_template('quest_10.html',
                               title='Квест "Скрытые секреты"',
                               riddle='Загадка 10: Жак Фреско',
                               fm='unhidden',
                               hide='hidden')


@app.route('/end')
def end():
    global username, time
    res = result()
    res.name = username
    res.timer = time
    db_sess = db_session.create_session()
    db_sess.add(res)
    db_sess.commit()
    db_sess = db_session.create_session()
    resu = db_sess.query(result)
    return render_template('end.html',
                           title='Квест "Скрытые секреты"',
                           username=username,
                           timer=time,
                           result=resu)


@app.route("/_timer", methods=["GET", "POST"])
def timer():
    global time
    new_time = t.decrement()
    time = str(datetime.timedelta(seconds=float(new_time)))
    return jsonify({"result": str(datetime.timedelta(seconds=float(new_time)))})


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
