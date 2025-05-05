from flask import Flask
from departments import bp as departments_bp
from roles import bp as roles_bp

app = Flask(__name__)

# Реєстрація Blueprint
app.register_blueprint(departments_bp)
app.register_blueprint(roles_bp)

if __name__ == "__main__":
    app.run(debug=True)
