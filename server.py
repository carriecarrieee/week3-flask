from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """ Returns homepage."""

    return render_template("index.html")


@app.route("/templates/application-form", methods=["POST"])
def show_form():
    """ Shows application form."""

    return render_template("/templates/application-form.html")


@app.route("/templates/application-response")
def show_response():
    """ Shows application submittal response."""

    fname = request.form.get("firstname")
    lname = request.form.get("lastname")
    salary = request.form.get("salary")
    role = request.form.get("role")

    return render_template("/templates/application-response.html",
                           fname=fname,
                           lname=lname,
                           salary=salary,
                           role=role) 


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
