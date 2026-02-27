from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app.web.auth import auth_bp
from app.web.auth.forms import LoginForm, RegistrationForm
from app.services.auth_service import AuthService


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("web.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = AuthService.authenticate(form.email.data, form.password.data)
        if user:
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("web.index"))
        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("web.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = AuthService.register(
            email=form.email.data,
            password=form.password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        if user:
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("auth.login"))
        flash("Email already registered.", "danger")

    return render_template("auth/register.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))