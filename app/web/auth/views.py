from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.services.auth_service import AuthService
from app.tasks.send_email import send_reset_email
from app.web.auth import auth_bp
from app.web.auth.forms import (
    ForgotPasswordForm,
    LoginForm,
    RegistrationForm,
    ResetPasswordForm,
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("web.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = AuthService.authenticate(form.email.data, form.password.data)
        if user:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            flash(f"Welcome back, {user.first_name}!", "success")
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
            return redirect(url_for("web.auth.login"))
        flash("Email already registered.", "danger")

    return render_template("auth/register.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("web.auth.login"))


@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for("web.index"))

    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = AuthService.get_by_email(form.email.data)
        if user:
            token = user.generate_reset_token()
            reset_url = url_for("auth.reset_password", token=token, _external=True)
            send_reset_email(current_app._get_current_object(), user.email, reset_url)

        # always show this message — don't reveal if email exists
        flash(
            "If that email is registered you will receive a reset link shortly.", "info"
        )
        return redirect(url_for("web.auth.login"))

    return render_template("auth/forgot_password.html", form=form)


@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = AuthService.get_by_reset_token(token)
    if not user:
        flash("This reset link is invalid or has expired.", "danger")
        return redirect(url_for("auth.forgot_password"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        success = AuthService.reset_password(token, form.password.data)
        if success:
            flash("Password reset successful. Please log in.", "success")
            return redirect(url_for("web.auth.login"))
        flash("Something went wrong. Please try again.", "danger")

    return render_template("auth/reset_password.html", form=form, token=token)
