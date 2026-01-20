from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    issue = request.form["issue"]
    priority = request.form["priority"]

    db = get_db()
    db.execute(
        "INSERT INTO tickets (name, issue, priority, status) VALUES (?, ?, ?, ?)",
        (name, issue, priority, "Open")
    )
    db.commit()
    db.close()

    return redirect("/")

@app.route("/admin")
def admin():
    db = get_db()
    tickets = db.execute("SELECT * FROM tickets").fetchall()
    db.close()
    return render_template("admin.html", tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
