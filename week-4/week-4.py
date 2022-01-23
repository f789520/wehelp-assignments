
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app = Flask(__name__,
            static_folder="publicFlaskTest",
            static_url_path="/")
app.secret_key = "test"

passwordlist = {"test":"test"}

@app.route("/")
def index():
    return render_template("index_week-4.html")

@app.route("/signin", methods=["POST"])
def signin():
    if  request.form["password"] == passwordlist.get(request.form["username"]):
        session["save_name"]=request.form["username"]
        return redirect("http://127.0.0.1:3000/member")
    elif request.form["username"] == "" or request.form["username"] == None :
        session["save_name"]= None
        return redirect("http://127.0.0.1:3000/error?message=none")
    elif request.form["password"] == "" or request.form["password"] == None:
        session["save_name"]= None
        return redirect("http://127.0.0.1:3000/error?message=none")
    else:
        session["save_name"]= None
        return redirect("http://127.0.0.1:3000/error?message=wrong")

@app.route("/member")
def member():
    # 不能寫讀取別頁的資訊 request.args.get("username") = = 
    if   session["save_name"] in passwordlist  :
        return render_template("member_week-4.html")
    elif session["save_name"] not in  passwordlist :
        return redirect("http://127.0.0.1:3000/")
    elif session["save_name"]== "" :
        return redirect("http://127.0.0.1:3000/")
    elif session["save_name"]== None :
        return redirect("http://127.0.0.1:3000/")
    else :
        return redirect("http://127.0.0.1:3000/")

@app.route("/error")
def error():
    a = request.args.get("message")
    if a == "none":
        return render_template("none_week-4.html")
    elif a == "wrong":
        return render_template("error_week-4.html")
    else:
        return render_template("error_week-4.html")


@app.route("/signout")
def signout():
    session["save_name"] = None
    return render_template("signout_week-4.html")


app.run(port=3000)
