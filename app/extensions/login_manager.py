from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "web.auth.login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User

    return User.query.get(user_id)  # removed int() — id is a UUID string
