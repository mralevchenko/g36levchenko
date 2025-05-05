from flask import Blueprint, render_template, request, redirect, url_for
from your_project import db
from your_project.models import Role  # Припустимо, є модель Role

bp = Blueprint('roles', __name__, url_prefix='/roles')

# Створюємо маршрут для перегляду списку ролей
@bp.route("/index")
def index():
    roles = Role.query.all()  # Отримуємо всі ролі з бази даних
    return render_template("roles/index.html", roles=roles)

# Створюємо маршрут для створення нової ролі
@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]  # отримуємо ім'я ролі з форми
        new_role = Role(name=name)
        db.session.add(new_role)
        db.session.commit()  # зберігаємо нову роль у базі даних
        return redirect(url_for("roles.index"))  # Перенаправляємо на список ролей

    return render_template("roles/create.html")  # Відображаємо форму для створення ролі

