from flask import Blueprint, render_template


bank_app = Blueprint('bank_app', __name__, url_prefix='/bank')


@bank_app.route('/')
def bank_page():
    return render_template('pages/bank/bank_page.html')
