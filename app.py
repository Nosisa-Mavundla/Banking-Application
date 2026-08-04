# Bringing the flask framework to our python file
from flask import Flask, render_template, request, session, redirect
from database import create_tables, get_connection
# create our flask app

app = Flask(__name__)
app.secret_key = "secrete_key"
# the homepage fuction


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # read values from the form
        full_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["password"]

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
INSERT INTO users(full_name, email, password)
VALUES(?,?,?)
        """, (full_name, email, password))

        connection.commit()
        connection.close()

        return "Your Account was created successfully!"

# if the user is simply visiting the page
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # read info fromthe form
        email = request.form["email"]
        password = request.form["password"]

# get connection
        connection = get_connection()
        cursor = connection.cursor()

# read from the db table for users identity verification

        cursor.execute("""
SELECT * FROM users
WHERE email = ?
   """, (email,))

        user = cursor.fetchone()
        connection.close()
# Application makes a decison whether tolet the user in
        if user:
            if password == user[3]:
                session["id"] = user[0]
                return redirect("/dashboard")
            else:
                return "Incorect password!"
        else:
            return " User does not exist!"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "id" not in session:
        return redirect("/login")
# if user id is in session flask retrives the session
    id = session["id"]
# connect to database /open db
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT*FROM users
    WHERE id =?

   """, (id,))

    user = cursor.fetchone()
    connection.close()

    full_name = user[1]

    return render_template("dashboard.html", full_name=full_name)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


create_tables()

if __name__ == "__main__":
    app.run(debug=True)
