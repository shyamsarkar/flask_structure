from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(name="Buyee", template_mode="bootstrap4")


class SecureModelView(ModelView):
    def is_accessible(self):
        return True  # later: role / auth check

    def inaccessible_callback(self, name, **kwargs):
        return "Unauthorized"
