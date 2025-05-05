from flask import Blueprint, render_template, request, redirect, url_for
from your_project import db
from your_project.models import Department  # Припустимо, є модель Department

bp = Blueprint('departments', __name__, url_prefix='/departments')

# Створюємо маршрут для перегляду списку департаментів
@bp.route("/index")
def index():
    departments = Department.query.all()  # Отримуємо всі департаменти з бази даних
    return render_template("departments/index.html", departments=departments)

# Створюємо маршрут для створення нового департаменту
@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]  # отримуємо ім'я департаменту з форми
        new_department = Department(name=name)
        db.session.add(new_department)
        db.session.commit()  # зберігаємо новий департамент у базі даних
        return redirect(url_for("departments.index"))  # Перенаправляємо на список департаментів

    return render_template("departments/create.html")  # Відображаємо форму для створення департаменту

