from flask import Flask
from flask_mysqldb import MySQL
import os

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    
    # Carregar configurações do arquivo .env ou config.py
    app.config.from_mapping(
        MYSQL_HOST=os.getenv("DB_HOST"),
        MYSQL_USER=os.getenv("DB_USER"),
        MYSQL_PASSWORD=os.getenv("DB_PASSWORD"),
        MYSQL_DB=os.getenv("DB_NAME"),
        GOOGLE_MAPS_API_KEY=os.getenv("GOOGLE_MAPS_API_KEY")
    )
    
    mysql.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app