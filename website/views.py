from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

names_list = ["Afnan", "Hassan", "Ali", "Usman", "Hussain", "Saad", "Umar"]


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_item = request.form.get("new_item_name")
        if new_item:
            names_list.append(new_item)
    return render_template("index.html", list=names_list)
