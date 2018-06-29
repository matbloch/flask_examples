from flask import render_template
from . import admin
from flask_security import login_required


# example file browsing
@admin.route('/')
@login_required
def admin_dashboard():
    return render_template('page/admin/index.html', title="Admin area")
