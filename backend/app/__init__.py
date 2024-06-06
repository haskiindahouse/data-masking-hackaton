from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.db_manager import bp as db_manager_bp
    app.register_blueprint(db_manager_bp, url_prefix='/db')

    from app.anonymization import bp as anonymization_bp
    app.register_blueprint(anonymization_bp, url_prefix='/anonymize')

    from app.reports import bp as reports_bp
    app.register_blueprint(reports_bp, url_prefix='/reports')

    from app.admin_dashboard import bp as admin_dashboard_bp
    app.register_blueprint(admin_dashboard_bp, url_prefix='/admin')

    return app