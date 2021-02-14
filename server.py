from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = "admin"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/process_money", methods=['POST'])
def findgold():
    if request.form["findgold"] == "farm":
        session["gold"] += random.randint(10,20)
        return redirect ("/")

    if request.form["findgold"] == "cave":
        session["gold"] += random.randint(5,10)
        return redirect ("/")

    if request.form["findgold"] == "house":
        session["gold"] += random.randint(2,5)
        return redirect ("/")

    if request.form["findgold"] == "casino":
        luck = random.randint(1,2)
        if luck == 1:
            session["gold"] += random.randint(1,50)
            return redirect ("/")
        else:
            session["gold"] -= random.randint(1,50)
            return redirect ("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
