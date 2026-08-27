from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("public/home.html")

@main.route("/faculty")
def faculty():
    return render_template("public/faculty.html")

@main.route("/research-verticals")
def research_verticals():
    return render_template("public/research.html")

@main.route("/sponsors")
def sponsors():
    return render_template("public/sponsors.html")