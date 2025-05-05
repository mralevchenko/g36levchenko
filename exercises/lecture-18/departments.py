from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from your_project import db
from your_project.models import Department

bp = Blueprint("departments", __name__, url_prefix="/departments")

@bp.route("/index")
@login_required
def index():
    departments = Department.query.all()
    return render_template("departments/index.html", departments=departments)

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        name = request.form["name"]
        if not name:
            flash("Department name is required.")
        else:
            new_department = Department(name=name)
            db.session.add(new_department)
            db.session.commit()
            flash("Department created successfully.")
            return redirect(url_for("departments.index"))
    return render_template("departments/create.html")

@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    department = Department.query.get_or_404(id)
    if request.method == "POST":
        name = request.form["name"]
        if not name:
            flash("Department name is required.")
        else:
            department.name = name
            db.session.commit()
            flash("Department updated successfully.")
            return redirect(url_for("departments.index"))
    return render_template("departments/update.html", department=department)

@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash("Department deleted.")
    return redirect(url_for("departments.index"))

