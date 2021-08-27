from flask import Flask, render_template, url_for, request,redirect
import csv


app = Flask(__name__)

@app.route("/")
def myhome():
    return render_template("./index.html")


# @app.route("/work.html")
# def work():
#     return render_template("./work.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")

# # @app.route("/components.html")
# # def mycomp():
# #     return render_template("./components.html")

# @app.route("/works.html")
# def works():
#     return render_template("./works.html")

# @app.route("/about.html")
# def aboutme():
#     return render_template("./about.html")

@app.route("/<string:page_name>")
def dynamic_pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt",mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open("database.csv",mode="a",newline='') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2,delimiter =",",quotechar= "~",quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect("./thanks.html")
        except:
            return " Try again!!"
    else:
        return "Something is wrong, Maybe re-submit!"
    return "Form is submitted! Thanks for your interest."
