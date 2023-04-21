from flask import Flask, render_template, url_for, redirect, flash,current_app
import os
import sys
import click
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
from flask_cors import CORS
import ssl

from booksapi import *
from bookstool import *
from setting import *

import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart,Response,request


# app = Flask(__name__)
app = Quart(__name__)


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/cat')
def cat():
    return render_template('pwa.html')




@app.route('/books', methods=['GET', 'POST'])
async def books():
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



@app.route('/')
def index():
    with current_app.app_context():
        return render_template('index.html')

@app.route("/test")
async def testa():
    return Response("ffff")


if __name__ == "__main__":
    # app.run(host="localhost", port=8000, use_http3=True)
    config = Config()
    config.bind = ["localhost:1235"]
    # config.quic_bind = ["localhost:8443"]

    # config.alpn_protocols = ["h3"]
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # ssl_context.load_cert_chain('/home/vajor/openssl/cert.pem', '/home/vajor/openssl/key.pem',password='vajors123')
    # config.ssl = ssl_context
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(serve(app, config))




