from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from controller.expense_api import expense_api
from controller.user_api import user_api
from flasgger import Swagger
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/convin'

app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
jwt = JWTManager(app)

db.init_app(app)  # Initialize db
migrate = Migrate(app, db)
swagger = Swagger(app)

app.register_blueprint(user_api)
app.register_blueprint(expense_api)

if __name__ == '__main__':
    app.run(debug=True)
