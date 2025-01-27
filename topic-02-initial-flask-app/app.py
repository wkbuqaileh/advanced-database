from flask import Flask, render_template
import sqlite3

# remember to $ pip install flask


connection = sqlite3.connect("pets.db", check_same_thread=False)

app = Flask(__name__)

@app.route("/", methods=["GET"]) 
def get_index():
    return("Example flask server.")

@app.route("/hello", methods=["GET"]) 
@app.route("/hello/<name>", methods=["GET"]) 
def get_hello(name="world"):
    data = [
        {"name":"bob","age":10},
        {"name":"suzy","age":8},
    ]
    return render_template("hello.html", data=data, prof={"name":name, "title":"Dr."})

@app.route("/bye", methods=["GET"])
def get_bye():
    return("Well, goodbye, then!")

@app.route("/list", methods=["GET"])
def get_list():
    cursor = connection.cursor()
    cursor.execute("""select * from pets where type=?""",("dog",))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render_template("list.html", rows=rows) 
