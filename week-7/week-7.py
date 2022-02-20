
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import mysql.connector
from flask.json import jsonify
from mysql.connector import Error
import pymysql.cursors
import pandas as pd
import json
from json import dumps
from urllib.parse import parse_qs
import sqlite3


# ------------------------------------MySQL 連線
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="88888888",
    db="website",
    charset="utf8",
)
mycursor = mydb.cursor(dictionary=True)
# ------------------------------------Flask 伺服器
app = Flask(__name__,
            static_folder="publicFlaskTest",
            static_url_path="/")
app.secret_key = "test"


@app.route("/")
def index():
    return render_template("index_week-6.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT * FROM member WHERE username='%s' and password='%s'" % (
        username, password)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult == None:
        return redirect("http://127.0.0.1:3000/error?message=帳號、或密碼輸入錯誤")
    session["nickname"] = myresult['name']

    return redirect("http://127.0.0.1:3000/member")


@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member_week-7.html", nickname=session["nickname"])
    else:
        return redirect("http://127.0.0.1:3000/")


@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error_week-6.html", message=message)


@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("http://127.0.0.1:3000/")


@app.route("/signup", methods=["POST"])
def signup():
    nickname = request.form["nickname"]
    username = request.form["usernameup"]
    password = request.form["passwordup"]
    sql = "SELECT 'name','username','password' FROM member WHERE username =%s"
    user = (username,)
    mycursor.execute(sql, user)
    myresult = mycursor.fetchone()
    if myresult != None:
        return redirect("http://127.0.0.1:3000/error?message=帳號已經被註冊")
    elif nickname == "":
        return redirect("http://127.0.0.1:3000/error?message=姓名、帳號、密碼不能為空白")
    elif username == "":
        return redirect("http://127.0.0.1:3000/error?message=姓名、帳號、密碼不能為空白")
    elif password == "":
        return redirect("http://127.0.0.1:3000/error?message=姓名、帳號、密碼不能為空白")

    sql = "INSERT INTO member (name,username,password) VALUES (%s, %s, %s)"
    val = (nickname, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect("http://127.0.0.1:3000/")

# http://127.0.0.1:3000/api/members?username=

@app.route("/api/members")
def members():
    username = request.args.get("username")  # 從網站網址列得到要查詢的帳號
    sql = "SELECT id,name,username FROM member WHERE username='%s'" % (
        username,)  # 從SQL查詢帳號 , '' 引號拿掉
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult == None:  
        return "{\"data\":null}"
    # 中文顯示 https://iii.run/archives/98b692d3d018.html
    return json.dumps(myresult, ensure_ascii=False)

@app.route("/search")
def search():
    search = request.args.get('search') #抓到FETCH 送的 string 資料(使用者查詢的輸入框資料)
    sql = "SELECT name,username FROM member WHERE username='%s'" % (
        search,)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult == None:
        return "查無姓名"
 
    search = json.dumps(myresult, ensure_ascii=False)
    data = json.loads(search)
    search_data = data.get("name")+" ("+data.get("username")+")"
    return search_data

app.run(port=3000)
