import os
from flask import Flask, flash, request, redirect, url_for, render_template
import json
from PIL import Image

# creating a image object (main image)


# save a image using extension

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = './static/img/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/galery', methods=['GET', 'POST'])
def galery():
    if request.method == 'POST':
        file = request.files['file']
        photos = []
        for i in os.listdir(app.config['UPLOAD_FOLDER'] + 'carousel/'):
            photos.append(i[:i.index(".")])
        f = open(os.path.join(app.config['UPLOAD_FOLDER'] + 'carousel/', f"{len(photos) + 1}.jpg"), 'w+')
        f.close()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'carousel/', f"{len(photos) + 1}.jpg"))
        return redirect(url_for('galery'))
    else:
        photos = []
        for i in os.listdir(app.config['UPLOAD_FOLDER'] + 'carousel/'):
            photos.append(i)
        return render_template('carousel.html', photos=photos[1:], length=list(range(1, len(photos))))


@app.route('/table_param/<gender>/<int:age>')
def table_param(gender, age):
    wall = ""
    if gender in ["male", "female"]:
        if gender == "male":
            photo = "male"
            wall = "blue"
        else:
            photo = "female"
            wall = "purple"
        if age >= 21:
            photo += "_2"
            wall += "-dark"
        else:
            photo += "_1"
            wall += "-light"
    else:
        photo = "no_gender"
        wall = "green"
    photo += ".jfif"
    wall += ".jfif"
    return render_template('rooms.html', wall=wall, photo=photo)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    person = {}
    person["title"] = "Анкета"
    person["name"] = "Andrew"
    person["surname"] = "Bokhonov"
    person["education"] = "курсы Академии Яндекса"
    person["profession"] = "программист"
    person["sex"] = "male"
    person["motivation"] = "как-то скучно тут"
    person["ready"] = False
    return render_template('auto_answer.html', **person)


@app.route('/member')
def member():
    with open("astronauts.json", encoding="utf-8") as f:
        members = json.load(f)
    return render_template('members.html', members=members)


@app.route('/distribution')
def distribution():
    person = ["Екатерина Владимировна", "Алиса Шапочкина", "Александр Астафуров", "Елена Старостина",
              "Андрей Бохонов", "Емелин Николай", "Александр Котиков", "Женя Строков", "Юля Федорищева"]
    return render_template('distribution.html', person=person)


@app.route('/load_photo', methods=['GET', 'POST'])
def upload_file():
    try:
        if request.method == 'POST':
            file = request.files['file']
            f = open(os.path.join(app.config['UPLOAD_FOLDER'], "photo.jpg"), 'w+')
            f.close()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "photo.jpg"))
            return redirect(url_for('upload_file'))
        else:
            return f'''<!doctype html>
                            <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
        <title>Пример формы</title>
    </head>
    <body>
    <h1 class = "form_h1">Загрузка фотографии для участия в миссии</h1>
    <div>
        <form class="upload" method="post" enctype=multipart/form-data>
            <div class="form-group">
                <label for="photo">Приложите фотографию</label>
                <input type="file" class="form-control-file" id="photo" name="file">
            </div>
            <img src="/static/img/photo.jpg" alt="у нас нет вашей фотографии..." class = "avatar">
            <button type="submit" class="btn btn-primary">Записаться</button>
        </form>
    </div>
    </body>
    </html>'''
    except Exception as e:
        print(e)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def prom():
    return "<p>Человечество вырастает из детства.</p>" \
           "<p>Человечеству мала одна планета.</p>" \
           "<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>" \
           "<p>И начнем с Марса!</p>" \
           "<p>Присоединяйся!</p>"


@app.route("/image_mars")
def image():
    return '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
    <title>Колонизация</title>
</head>
<body>
    <h1 class = "title">Жди нас, Марс</h1>
    <img src="/static/img/mars.jpg" alt="Grapefruit slice atop a pile of other slices">
    <div><p class = "first">Человечество вырастает из детства.</p>
           <p class = "second">Человечеству мала одна планета.</p>
           <p class = "first">Мы сделаем обитаемыми безжизненные пока планеты.</p>
           <p class = "third">И начнем с Марса!</p>
           <p class = "fourth">Присоединяйся!</p></div>
    </body>
    '''


@app.route("/choice/<planet_name>")
def choice(planet_name):
    data = []
    if planet_name == "Марс":
        data = ["он красный, это очень важно",
                "там никого не было, круто будет оказаться там впервые",
                "он близко к Земле, даже до кванториума ехать дальше, чем до Марса...",
                "туда все хотят поселиться, разве мы хуже?"]
    elif planet_name == "Юпитер":
        data = ["он большой",
                "у него 80 спутников, а с соседями, как известно, веселее",
                "он в самом центре Солнечной системы, а люди любят быть в центре внимания",
                "Юпитер - газовый гигант, значит мы будет не ходить, а летать..."]
    else:
        data = ["ну, если вы выбрали эту планету, она не такая плохая",
                "возможно никто кроме вас туда не хочет, но зато никто мешать не будет!",
                "в конце концов, кто не рискует, тот не пьет шампанского...",
                "помните: гении часто остаются непонятыми"]
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
        <title>Колонизация</title>
    </head>
    <body>
        <h1>Мое предложение: {planet_name}</h1>
        <div><p class = "first">{data[0]}</p>
               <p class = "second">{data[1]}</p>
               <p class = "first">{data[2]}</p>
               <p class = "third">{data[3]}</p>
    </body>
    '''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def result(nickname, level, rating):
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
        <title>Результаты</title>
    </head>
    <body>
        <h1>Результаты отбора</h1>
        <h2>Претендента на участие в миссии {nickname}</h2>
        <p class = "first">Поздравляем! Ваш рейтинг после {str(level)} этапа отбора</p>
        <p class = "second">составляет {str(rating)}</p>
        <p class = "first">Желаем удачи!</p>
    </body>
    '''


@app.route("/carousel")
def carousel():
    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="/static/css/style.css"/>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <title>Результаты</title>
    </head>
    <body>
        <h1>Пейзажи Марса</h1>
        <div class="container">
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="/static/img/mars1.jpg" style="width:100%;">
      </div>

      <div class="item">
        <img src="/static/img/mars2.jpg" style="width:100%;">
      </div>
    
      <div class="item">
        <img src="/static/img/mars3.jpg" style="width:100%;">
      </div>
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>
</body>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
