from flask import Flask, render_template  # import Flask class from a flask framework

# render_template() access an html file stored somewhere in python file

app = Flask(__name__)  # instantiating get name of the script


@app.route('/')  # this is a decorator
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
 