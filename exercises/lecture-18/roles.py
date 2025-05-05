from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from your_project import db
from your_project.models import Role

bp = Blueprint("roles", __name__, url_prefix="/roles")

@bp.route("/index")
@login_required
def index():
    roles = Role.query.all()
    return render_template("roles/index.html", roles=roles)

@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        name = request.form["name"]
        if not name:
            flash("Role name is required.")
        else:
            new_role = Role(name=name)
            db.session.add(new_role)
            db.session.commit()
            flash("Role created successfully.")
            return redirect(url_for("roles.index"))
    return render_template("roles/create.html")

@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    role = Role.query.get_or_404(id)
    if request.method == "POST":
        name = request.form["name"]
        if not name:
            flash("Role name is required.")
        else:
            role.name = name
            db.session.commit()
            flash("Role updated successfully.")
            return redirect(url_for("roles.index"))
    return render_template("roles/update.html", role=role)

@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash("Role deleted.")
    return redirect(url_for("roles.index"))
