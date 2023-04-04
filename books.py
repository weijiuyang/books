from flask import Flask, render_template,request, url_for, redirect, flash
import os
import sys
import click
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类


from booksapi import *
from bookstool import *
from setting import *

app = Flask(__name__)

app.config['CUSTOM_STATIC_PATH'] = "/home/vajor/advance/path"

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份

@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index'))  # 重定向回主页
        # 保存表单数据到数据库
        movie = Movie(title=title, year=year)  # 创建记录
        db.session.add(movie)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index'))  # 重定向回主页
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有电影记录
    return render_template('index.html', user=user, movies=movies)

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/books', methods=['GET', 'POST'])
def books():
    # 获取表单数据
    id = request.args.get('id')  # 传入表单对应输入字段的 name 值
    if id:
        essay_info = id_essay(id)[0]
    else:
        essay_info = random_essay("essay")[0]
        id = essay_info[0]

    print(essay_info[1])
    if essay_info[1] == "": 
        essay_address = essay_info[3]
        title,text,audiolist = linkaudio(publication_path,essay_address)
        essays_list = coadvance(id)

        return render_template('books.html', text = text,title = title, essays = essays_list,audiolist = audiolist)


    else:
        essay_address = pixiv_path +  essay_info[3]

        title, website, description, keywords, text = divide(essay_address)
        series_front = essay_info[8]
        series_left = essay_info[9]
        series_right = essay_info[10]
        series_name = essay_info[7]
        author_name = essay_info[14]
        essays_list = coadvance(id)


        return render_template('books.html', text = text, title = title,series_front = series_front, 
                 essays = essays_list, series_left = series_left , series_right = series_right,\
                keywords = keywords, id = id)


    # title,text,audiolist = linkaudio(essay_address)
    return render_template('books.html', text = text,title = title, essays = essays_list,audiolist = audiolist)
    title, website, description, keywords, text = divide(essay_address)
    # keywords = keywordsstring.split(",")
    mainimg(essay_address)
    # os.copy2(essay_address)

    is_series = essay_info[7]

    if is_series:
        series_front = essay_info[8]
        series_left = essay_info[9]
        series_right = essay_info[10]
        series_name = essay_info[7]
        author_name = essay_info[14]

        return render_template('books.html', text = text, title = title, is_series = is_series,\
                series_front = series_front, series_left = series_left , series_right = series_right,\
                keywords = keywords, id = id)
    else:
        return render_template('books.html', text = text, title = title, is_series = is_series,\
                keywords = keywords, id = id)


@app.route('/wait', methods=['GET', 'POST'])
def wait():
    info = random_essay("wait")[0]
    id = info[0]
    title = info[1]
    wait_address = wait_path + str(info[2])
    try:
        with open(wait_address, "r", encoding="gbk") as f :
            text = f.read()
    except: 
        with open(wait_address, "r") as f :
            text = f.read()

    print(wait_address)
    return render_template('wait.html', id = id, title = title, text = text)


@app.route('/essay/deleted', methods=['GET', 'POST'])
def delete_essay_():
    essay_id = request.args.get('essay_id') 
    delete_essay(essay_id)
    return redirect(url_for('books',))

@app.route('/wait/deleted', methods=['GET', 'POST'])
def delete_wait_():
    id = request.args.get('id') 
    delete_wait(id)
    return redirect(url_for('wait'))

@app.route('/wait/saved', methods=['GET', 'POST'])
def save_wait_():
    id = request.args.get('id') 
    save_wait(id)
    
    return redirect(url_for('wait'))

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    user = User.query.first()
    return render_template('404.html', user=user), 404  # 返回模板和状态码

# server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
# server.serve_forever()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='1234', debug=True)






