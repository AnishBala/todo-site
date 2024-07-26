from flask import Flask, render_template, request, redirect, url_for
import csv 


app = Flask(__name__)

@app.route("/")
def index():
    with open('todo.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        todo_list = [ row ["list"] for row in reader]
    return render_template("site.html", todo_list = todo_list)
@app.route("/", methods = ["POST"])
def add_item():
    with open('todo.csv', "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["list"])
        writer.writerow({"list": request.form.get("todoitem")})
    return redirect(url_for("index"))
app.run()
