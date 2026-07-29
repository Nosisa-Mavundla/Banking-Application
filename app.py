# Bringing the flask framework to our python file
from flask import Flask, render_template, request
from database import create_tables, get_connection
# create our flask app

app = Flask(__name__)

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


create_tables()

if __name__ == "__main__":
    app.run(debug=True)
