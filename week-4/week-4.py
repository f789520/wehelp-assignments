from email import message
from flask import Flask  
from flask import request  
from flask import render_template  
from flask import redirect
from flask import session

app = Flask(__name__,
            static_folder="publicFlaskTest",
            static_url_path="/")
app.secret_key="test"
cor_username = "test"
cor_password = "test"

@app.route("/")
def index():
    return render_template("index_week-4.html")
    
@app.route("/signin", methods=["POST"])
def signin():
    session["save_name"]=request.form["username"]
    if request.form["username"] == cor_username and request.form["password"] == cor_password:
        return redirect("http://127.0.0.1:3000/member")
    elif request.form["username"] == "" or request.form["password"] == "":
        return redirect("http://127.0.0.1:3000/error?message=none")
    elif cor_username != request.form["username"] or request.form["password"] != cor_username:
        return redirect("http://127.0.0.1:3000/error?message=wrong")

@app.route("/member")
def member():
    session["save_name"]
    if session["save_name"]==None:
        return redirect("http://127.0.0.1:3000/")
    else:
        return render_template("member_week-4.html")

@app.route("/error")
def error():
    a = request.args.get("message")
    if a == "none":
        return render_template("none_week-4.html")
    else:
        return render_template("error_week-4.html")

@app.route("/signout")
def signout():
    session["save_name"]=None
    return render_template("signout_week-4.html")

app.run(port=3000)
