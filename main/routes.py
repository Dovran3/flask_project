from main import app
from main import db
from flask import render_template, request, redirect
from main.models import Info


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		comment = request.form["comment"]
		db.session.add(Info(name=name, email=email, comment=comment))
		db.session.commit()
		return redirect("/blog")
	return render_template("blog.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/course")
def course():
	return render_template("course.html")

@app.route("/allposts", methods=["GET", "POST"])
def allposts():
	persons = Info.query.all()
	return render_template("allposts.html", persons=persons)
